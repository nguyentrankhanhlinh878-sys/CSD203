"""
Comprehensive Test Suite for Smart Elevator Dispatch Simulator.
CSD203 - Data Structures and Algorithms (FA26)
"""

import unittest
import sys
import os

# Add src/ to sys.path so tests can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import io
from unittest.mock import patch
from data_structures import MinHeap, MaxHeap, FIFOQueue
from models import Elevator, ElevatorState, Direction, ExternalRequest, CabinRequest
from dispatcher import GroupDispatcher
from main import parse_elevators_input, parse_external_requests, parse_cabin_requests, display_results, run_simulator


class TestCustomDataStructures(unittest.TestCase):
    def test_min_heap(self):
        heap = MinHeap()
        values = [7, 2, 9, 1, 5, 8, 3]
        for v in values:
            heap.insert(v)

        sorted_out = []
        while not heap.is_empty():
            sorted_out.append(heap.extract_min())

        self.assertEqual(sorted_out, sorted(values))
        self.assertTrue(heap.is_empty())

    def test_max_heap(self):
        heap = MaxHeap()
        values = [7, 2, 9, 1, 5, 8, 3]
        for v in values:
            heap.insert(v)

        sorted_out = []
        while not heap.is_empty():
            sorted_out.append(heap.extract_max())

        self.assertEqual(sorted_out, sorted(values, reverse=True))
        self.assertTrue(heap.is_empty())

    def test_fifo_queue(self):
        q = FIFOQueue()
        for i in range(10):
            q.enqueue(i)

        self.assertEqual(len(q), 10)
        self.assertEqual(q.peek(), 0)

        results = []
        while not q.is_empty():
            results.append(q.dequeue())

        self.assertEqual(results, list(range(10)))
        self.assertTrue(q.is_empty())


class TestElevatorLOOKRoute(unittest.TestCase):
    def test_idle_elevator_no_stops(self):
        elev = Elevator(1, initial_floor=4)
        self.assertFalse(elev.has_movement())
        self.assertEqual(elev.generate_route(), [4])

    def test_elevator_moving_up_sweep(self):
        elev = Elevator(1, initial_floor=2, initial_dest=8)
        elev.add_stop(5, Direction.UP)
        elev.add_stop(11, Direction.UP)
        # Add stop below, should sweep after
        elev.add_stop(1, Direction.DOWN)

        route = elev.generate_route()
        self.assertEqual(route, [2, 5, 8, 11, 1])

    def test_elevator_moving_down_sweep(self):
        elev = Elevator(2, initial_floor=9, initial_dest=3)
        elev.add_stop(7, Direction.DOWN)
        elev.add_stop(12, Direction.UP)

        route = elev.generate_route()
        self.assertEqual(route, [9, 7, 3, 12])


class TestDispatcherAndEdgeCases(unittest.TestCase):
    def setUp(self):
        # 10 Elevators setup: 12 Floors
        # E1: 1, E2: 3, E3: 5:10 (moving up), E4: 8:2 (moving down), E5..E10: 4, 6, 7, 9, 11, 12
        input_str = "1 3 5:10 8:2 4 6 7 9 11 12"
        self.elevators = parse_elevators_input(input_str)
        self.dispatcher = GroupDispatcher(self.elevators, total_floors=12)

    def test_en_route_pickup_tier1(self):
        # E3 is at 5 going to 10. External call 7U should go to E3 with cost 7 - 5 = 2.
        req_7u = ExternalRequest(7, Direction.UP)
        cost_e3 = self.dispatcher.calculate_cost(self.elevators[2], req_7u)
        self.assertEqual(cost_e3, 2)

        assigned_elev, cost = self.dispatcher.dispatch_external(req_7u)
        self.assertEqual(assigned_elev.id, 3)
        self.assertEqual(cost, 2)

    def test_simultaneous_up_and_down_same_floor(self):
        # Requests 6U and 6D
        req_6u = ExternalRequest(6, Direction.UP)
        req_6d = ExternalRequest(6, Direction.DOWN)

        elev_u, _ = self.dispatcher.dispatch_external(req_6u)
        elev_d, _ = self.dispatcher.dispatch_external(req_6d)

        # Both requests are assigned and served
        self.assertIn(6, elev_u.planned_stops)
        self.assertIn(6, elev_d.planned_stops)

    def test_multiple_cabin_requests_single_elevator(self):
        # Elevator 1 has cabin requests: 1:12, 1:4, 1:8
        c1 = CabinRequest(1, 12)
        c2 = CabinRequest(1, 4)
        c3 = CabinRequest(1, 8)

        self.dispatcher.process_cabin(c1)
        self.dispatcher.process_cabin(c2)
        self.dispatcher.process_cabin(c3)

        route = self.elevators[0].generate_route()
        # Initial floor is 1, targets are 4, 8, 12
        self.assertEqual(route, [1, 4, 8, 12])

    def test_idle_elevators_remain_without_movement(self):
        # Only assign request to Elevator 1
        self.dispatcher.process_cabin(CabinRequest(1, 5))

        # Check that untouched elevators (e.g. Elevator 2, 5, 6, 7, 8, 9, 10) have no movement
        self.assertFalse(self.elevators[1].has_movement())  # Elevator 2
        self.assertFalse(self.elevators[4].has_movement())  # Elevator 5
        self.assertTrue(self.elevators[0].has_movement())   # Elevator 1

    def test_idle_elevator_assigned_at_same_floor(self):
        # Bug 1 verification: IDLE elevator at floor 5 receives 5U
        elev = Elevator(1, initial_floor=5)
        added = elev.add_stop(5, Direction.UP)
        self.assertTrue(added)
        self.assertTrue(elev.has_movement())
        self.assertEqual(elev.state, ElevatorState.MOVING_UP)
        self.assertEqual(elev.generate_route(), [5])

    def test_look_route_behind_stops_monotonic(self):
        # Bug 2 verification: Elevator at 5 going to 10 receives 2U
        elev = Elevator(1, initial_floor=5, initial_dest=10)
        elev.add_stop(2, Direction.UP)
        route = elev.generate_route()
        self.assertEqual(route, [5, 10, 2])

    def test_idle_elevator_opposite_direction_compound(self):
        # Bug 3 verification: Elevator at 12 receives 2U and 8D
        elev = Elevator(2, initial_floor=12)
        elev.add_stop(2, Direction.UP)
        self.assertEqual(elev.state, ElevatorState.MOVING_DOWN)
        elev.add_stop(8, Direction.DOWN)
        route = elev.generate_route()
        self.assertEqual(route, [12, 8, 2])

    def test_generate_route_non_destructive(self):
        # Bug 4 verification: Calling generate_route twice leaves queues intact
        elev = Elevator(4, initial_floor=1, initial_dest=6)
        r1 = elev.generate_route()
        r2 = elev.generate_route()
        self.assertEqual(r1, [1, 6])
        self.assertEqual(r2, [1, 6])

    def test_parse_elevators_identical_dest_rejected(self):
        # Bug 6 verification: 3:3 should raise ValueError
        with self.assertRaises(ValueError):
            parse_elevators_input("1 2 3:3 4 5 6 7 8 9 10")

    def test_cabin_request_at_same_floor_log_handled(self):
        # Bug 7 verification: Cabin request 2:3 when E2 is at 3 idle is ignored gracefully
        logs = self.dispatcher.run_dispatch(FIFOQueue(), [CabinRequest(2, 3)])
        self.assertTrue(any("bỏ qua" in log.lower() for log in logs))

    def test_cli_parsers_validation(self):
        # Bug 8 test coverage: Test external and cabin request parsers
        ext_valid = parse_external_requests("1U 12D 5U 6D")
        self.assertEqual(len(ext_valid), 4)
        self.assertEqual(ext_valid[0].floor, 1)
        self.assertEqual(ext_valid[0].direction, Direction.UP)

        with self.assertRaises(ValueError):
            parse_external_requests("1D")  # Floor 1 cannot call down
        with self.assertRaises(ValueError):
            parse_external_requests("12U")  # Floor 12 cannot call up
        with self.assertRaises(ValueError):
            parse_external_requests("invalid")

        cab_valid = parse_cabin_requests("1:10 2:5")
        self.assertEqual(len(cab_valid), 2)
        self.assertEqual(cab_valid[0].elevator_id, 1)
        self.assertEqual(cab_valid[0].target_floor, 10)

        with self.assertRaises(ValueError):
            parse_cabin_requests("11:5")  # Elevator 11 out of range [1..10]
        with self.assertRaises(ValueError):
            parse_cabin_requests("1:15")  # Floor 15 out of range [1..12]

    def test_fifo_queue_compaction_triggered(self):
        # Bug 9 test coverage: Test compaction (> 50 dequeues)
        q = FIFOQueue()
        for i in range(120):
            q.enqueue(i)
        for i in range(70):
            self.assertEqual(q.dequeue(), i)
        # Verify compaction occurred and remaining elements are intact
        self.assertEqual(len(q), 50)
        self.assertEqual(q.peek(), 70)

    def test_display_results_step_by_step(self):
        # Test display_results with active movement
        elevators = parse_elevators_input("1 3 5:10 8:2 4 6 7 9 11 12")
        elevators[0].add_stop(12, Direction.UP)
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            display_results(elevators, ["Sample log"])
        finally:
            sys.stdout = old_stdout

        output_str = captured_output.getvalue()
        self.assertIn("NHẬT KÝ ĐIỀU PHỐI", output_str)
        self.assertIn("BẢNG CÁC BƯỚC DI CHUYỂN CỦA THANG MÁY", output_str)
        self.assertIn("Vị trí đầu", output_str)
        self.assertIn("Đích 1", output_str)
        self.assertIn("#1", output_str)
        self.assertIn("↑ 12", output_str)
        self.assertIn("↑ 10", output_str)
        self.assertIn("↓ 2", output_str)
        self.assertNotIn("TỔNG KẾT LỘ TRÌNH CUỐI CÙNG", output_str)

        # Completed movement updates the position and clears stops for the next batch.
        self.assertEqual(elevators[0].current_floor, 12)
        self.assertFalse(elevators[0].has_movement())
        self.assertEqual(elevators[0].state, ElevatorState.IDLE)
        self.assertEqual(elevators[0].generate_route(), [12])

        dispatcher = GroupDispatcher(elevators, total_floors=12)
        dispatcher.process_cabin(CabinRequest(1, 5))
        self.assertEqual(elevators[0].generate_route(), [12, 5])

        # Test display_results when all elevators are idle
        idle_elevators = parse_elevators_input("1 2 3 4 5 6 7 8 9 10")
        captured_idle = io.StringIO()
        try:
            sys.stdout = captured_idle
            display_results(idle_elevators, [])
        finally:
            sys.stdout = old_stdout

        idle_str = captured_idle.getvalue()
        self.assertIn("Tất cả 10 thang máy đều ở trạng thái đứng yên", idle_str)

    def test_display_results_adapts_to_narrow_terminal(self):
        elevators = parse_elevators_input("1 2 3 4 5 6 7 8 9 10")
        for floor in range(2, 13):
            elevators[0].add_stop(floor, Direction.UP)

        captured_output = io.StringIO()
        with patch("shutil.get_terminal_size", return_value=os.terminal_size((40, 24))):
            with patch("sys.stdout", captured_output):
                display_results(elevators, ["A very long dispatch log " * 5])

        output = captured_output.getvalue()
        self.assertTrue(all(len(line) <= 40 for line in output.splitlines()))
        self.assertIn("Các điểm dừng (", output)
        self.assertIn("BẢNG CÁC BƯỚC DI CHUYỂN", output)

    def test_cli_can_continue_and_reset_elevator_positions(self):
        inputs = [
            "1 2 3 4 5 6 7 8 9 10",
            "",
            "1:3",
            "1",
            "",
            "1:5",
            "2",
            "2 3 4 5 6 7 8 9 10 11",
            "",
            "",
            EOFError,
        ]
        captured_output = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", captured_output):
            run_simulator()

        output = captured_output.getvalue()
        self.assertIn("[BƯỚC 1]", output)
        self.assertIn("[BƯỚC 2]", output)
        self.assertIn("[BƯỚC 3]", output)
        self.assertIn("<mã_thang>:<tầng_đích>", output)
        self.assertIn("↑ 3", output)
        self.assertIn("↑ 5", output)
        self.assertNotIn("TỔNG KẾT LỘ TRÌNH CUỐI CÙNG", output)
        self.assertIn("Giữ nguyên vị trí hiện tại", output)
        self.assertIn("Đặt lại toàn bộ thang", output)


if __name__ == "__main__":
    unittest.main()
