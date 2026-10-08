"""
Group Dispatcher for Smart Elevator System.
CSD203 - Data Structures and Algorithms (FA26)
Calculates multi-criteria cost function and dispatches requests.
"""

from typing import List, Tuple, Optional
from models import Elevator, ElevatorState, Direction, ExternalRequest, CabinRequest
from data_structures import FIFOQueue


class GroupDispatcher:
    """
    Coordinates 10 elevators in a 12-floor building.
    Uses cost-minimization function combined with LOOK heuristics.
    """
    def __init__(self, elevators: List[Elevator], total_floors: int = 12):
        self.elevators = elevators
        self.total_floors = total_floors

    def get_elevator(self, elevator_id: int) -> Elevator:
        return self.elevators[elevator_id - 1]

    def calculate_cost(self, elevator: Elevator, req: ExternalRequest) -> int:
        """
        Calculates dispatching cost for an elevator serving an external request.
        Tier 1 (Same direction, en-route): cost = direct_distance
        Tier 2 (IDLE elevator): cost = direct_distance + N
        Tier 3 (Opposite direction or already passed): cost = direct_distance + 2N
        """
        dist = abs(elevator.current_floor - req.floor)

        # Tier 1: Moving in same direction and has not passed the requested floor
        if elevator.state == ElevatorState.MOVING_UP and req.direction == Direction.UP:
            if elevator.current_floor <= req.floor:
                return dist
        elif elevator.state == ElevatorState.MOVING_DOWN and req.direction == Direction.DOWN:
            if elevator.current_floor >= req.floor:
                return dist

        # Tier 2: Elevator is IDLE
        if elevator.state == ElevatorState.IDLE:
            return dist + self.total_floors

        # Tier 3: Opposite direction or already passed
        return dist + (2 * self.total_floors)

    def dispatch_external(self, req: ExternalRequest) -> Tuple[Elevator, int]:
        """
        Selects the elevator with minimal cost for the external request and assigns it.
        """
        best_elevator = None
        min_cost = float("inf")

        for elevator in self.elevators:
            cost = self.calculate_cost(elevator, req)
            if cost < min_cost:
                min_cost = cost
                best_elevator = elevator

        best_elevator.add_stop(req.floor, req.direction)
        return best_elevator, min_cost

    def process_cabin(self, req: CabinRequest) -> bool:
        """Directly queues a cabin request to the specified elevator. Returns True if accepted."""
        elevator = self.get_elevator(req.elevator_id)
        return elevator.add_stop(req.target_floor)

    def run_dispatch(
        self,
        external_queue: FIFOQueue,
        cabin_requests: List[CabinRequest],
        down_queue: Optional[FIFOQueue] = None
    ) -> List[str]:
        """
        Executes the batch dispatching workflow:
        1. Inject cabin requests into corresponding elevator queues.
        2. Dispatch external hall calls sequentially in FIFO order.
           Supports either a single external_queue or direction-separated queues (up & down).
        """
        logs = []

        # 1. Process Cabin Requests first (passengers already aboard have highest urgency)
        for cab_req in cabin_requests:
            added = self.process_cabin(cab_req)
            if added:
                logs.append(
                    f"Yêu cầu trong cabin -> Thang máy #{cab_req.elevator_id} sẽ dừng tại tầng {cab_req.target_floor}"
                )
            else:
                logs.append(
                    f"Yêu cầu trong cabin -> Thang máy #{cab_req.elevator_id} bỏ qua tầng "
                    f"{cab_req.target_floor} (đang ở tầng này hoặc yêu cầu bị trùng)"
                )

        # 2. Dispatch all External Requests in FIFO sequence
        queues_to_process = [external_queue]
        if down_queue is not None:
            queues_to_process.append(down_queue)

        for q in queues_to_process:
            while not q.is_empty():
                ext_req = q.dequeue()
                assigned_elev, cost = self.dispatch_external(ext_req)
                dir_str = "LÊN" if ext_req.direction == Direction.UP else "XUỐNG"
                logs.append(
                    f"Yêu cầu gọi tầng {ext_req.floor} đi {dir_str} -> "
                    f"Giao cho thang máy #{assigned_elev.id} (chi phí: {cost})"
                )

        return logs
