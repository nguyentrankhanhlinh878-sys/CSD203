"""
Domain Models for Smart Elevator Dispatch Simulator.
CSD203 - Data Structures and Algorithms (FA26)
"""

from enum import Enum
from typing import List, Optional, Set
from data_structures import MinHeap, MaxHeap


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    NONE = "NONE"

    def __str__(self):
        return self.value


class ElevatorState(Enum):
    IDLE = "IDLE"
    MOVING_UP = "MOVING_UP"
    MOVING_DOWN = "MOVING_DOWN"

    def __str__(self):
        return self.value


class ExternalRequest:
    """Request from a floor hallway with intended travel direction."""
    def __init__(self, floor: int, direction: Direction):
        self.floor = floor
        self.direction = direction

    def __repr__(self):
        return f"External({self.floor}{'U' if self.direction == Direction.UP else 'D'})"


class CabinRequest:
    """Request made inside an elevator cabin targeting a specific floor."""
    def __init__(self, elevator_id: int, target_floor: int):
        self.elevator_id = elevator_id
        self.target_floor = target_floor

    def __repr__(self):
        return f"Cabin(E#{self.elevator_id} -> {self.target_floor})"


class Elevator:
    """
    Represents an elevator cabin equipped with dual-heap priority queues (LOOK algorithm).
    """
    def __init__(self, elevator_id: int, initial_floor: int, initial_dest: Optional[int] = None):
        self.id = elevator_id
        self.initial_floor = initial_floor
        self.current_floor = initial_floor
        self.initial_dest = initial_dest

        self.up_queue = MinHeap()
        self.down_queue = MaxHeap()
        self.planned_stops: Set[int] = set()

        # Determine initial state
        if initial_dest is not None and initial_dest != initial_floor:
            if initial_dest > initial_floor:
                self.state = ElevatorState.MOVING_UP
                self.up_queue.insert(initial_dest)
            else:
                self.state = ElevatorState.MOVING_DOWN
                self.down_queue.insert(initial_dest)
            self.planned_stops.add(initial_dest)
        else:
            self.state = ElevatorState.IDLE

    def add_stop(self, floor: int, dir_intent: Direction = Direction.NONE) -> bool:
        """
        Adds a stop floor into the appropriate heap.
        Uses per-queue deduplication so a floor CAN exist in both
        up_queue and down_queue (e.g. pickup UP at floor 5, drop-off DOWN at floor 5).
        Returns True if newly added, False if duplicate within the target queue.
        """
        # Redundant cabin call at current floor while idle
        if floor == self.current_floor and self.state == ElevatorState.IDLE and dir_intent == Direction.NONE:
            return False

        # Determine target queue
        target_up = False
        target_down = False

        if dir_intent == Direction.UP:
            target_up = True
        elif dir_intent == Direction.DOWN:
            target_down = True
        elif floor > self.current_floor:
            target_up = True
        elif floor < self.current_floor:
            target_down = True
        else:
            # floor == current_floor and elevator is not IDLE (moving through)
            # Default: place in the queue matching current travel direction
            if self.state == ElevatorState.MOVING_UP:
                target_up = True
            elif self.state == ElevatorState.MOVING_DOWN:
                target_down = True
            else:
                return False

        added = False
        if target_up:
            if not self.up_queue.contains(floor):
                self.up_queue.insert(floor)
                added = True
        elif target_down:
            if not self.down_queue.contains(floor):
                self.down_queue.insert(floor)
                added = True

        if added:
            self.planned_stops.add(floor)
            # Update state if was IDLE: determine physical direction of travel to first target
            if self.state == ElevatorState.IDLE:
                if floor > self.current_floor:
                    self.state = ElevatorState.MOVING_UP
                elif floor < self.current_floor:
                    self.state = ElevatorState.MOVING_DOWN
                else:
                    self.state = ElevatorState.MOVING_UP if dir_intent == Direction.UP else ElevatorState.MOVING_DOWN

        return added

    def has_movement(self) -> bool:
        """Returns True if the elevator has any stops to make."""
        return len(self.planned_stops) > 0

    def finish_route(self) -> None:
        """Clear completed stops and leave the elevator idle at its current floor."""
        self.up_queue = MinHeap()
        self.down_queue = MaxHeap()
        self.planned_stops.clear()
        self.initial_dest = None
        self.state = ElevatorState.IDLE

    def generate_route(self) -> List[int]:
        """
        Computes the complete, ordered route using the LOOK algorithm over the dual heaps.
        Uses non-destructive heap copies and Phased Monotonic LOOK to ensure
        strictly monotonic sweeps without backward jumps.
        """
        route = [self.current_floor]
        if not self.has_movement():
            return route

        curr = self.current_floor

        # Copy heaps so method is non-destructive
        up_copy = self.up_queue.copy()
        down_copy = self.down_queue.copy()

        # Extract all elements into sorted lists
        up_stops = []
        while not up_copy.is_empty():
            up_stops.append(up_copy.extract_min())

        down_stops = []
        while not down_copy.is_empty():
            down_stops.append(down_copy.extract_max())

        # Determine primary direction if was IDLE
        primary_dir = self.state
        if primary_dir == ElevatorState.IDLE:
            if up_stops and down_stops:
                dist_up = min(abs(s - curr) for s in up_stops)
                dist_down = min(abs(s - curr) for s in down_stops)
                primary_dir = ElevatorState.MOVING_UP if dist_up <= dist_down else ElevatorState.MOVING_DOWN
            elif up_stops:
                primary_dir = ElevatorState.MOVING_UP
            else:
                primary_dir = ElevatorState.MOVING_DOWN

        # Multi-phase Monotonic LOOK:
        # If moving UP:
        # Phase 1: All UP stops >= curr (ascending)
        # Phase 2: All DOWN stops (descending)
        # Phase 3: Any UP stops < curr behind initial floor (ascending)
        if primary_dir == ElevatorState.MOVING_UP:
            phase1 = [f for f in up_stops if f >= curr]
            phase2 = down_stops
            phase3 = [f for f in up_stops if f < curr]
            all_stops = phase1 + phase2 + phase3
        else:  # MOVING_DOWN
            # Phase 1: All DOWN stops <= curr (descending)
            # Phase 2: All UP stops (ascending)
            # Phase 3: Any DOWN stops > curr above initial floor (descending)
            phase1 = [f for f in down_stops if f <= curr]
            phase2 = up_stops
            phase3 = [f for f in down_stops if f > curr]
            all_stops = phase1 + phase2 + phase3

        for stop in all_stops:
            if stop != route[-1]:
                route.append(stop)

        return route
