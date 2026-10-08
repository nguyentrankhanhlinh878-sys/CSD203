"""
Command-Line Interface (CLI) for Smart Elevator Dispatch Simulator.
CSD203 - Data Structures and Algorithms (FA26)
Building: 12 Floors | Elevators: 10 Cabins
"""

import sys
import os
import re
import shutil
import textwrap
import unicodedata
from typing import List, Tuple

# Ensure modules in src are directly accessible
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from models import Elevator, Direction, ExternalRequest, CabinRequest
from data_structures import FIFOQueue
from dispatcher import GroupDispatcher

TOTAL_FLOORS = 12
TOTAL_ELEVATORS = 10


def _terminal_width() -> int:
    return max(20, shutil.get_terminal_size(fallback=(80, 24)).columns)


def _display_width(value: str) -> int:
    return sum(
        0 if unicodedata.combining(char) else 2 if unicodedata.east_asian_width(char) in ("F", "W") else 1
        for char in value
    )


def _print_wrapped(text: str, continuation_indent: str = "   "):
    width = _terminal_width()
    lines = textwrap.wrap(
        text,
        width=width,
        subsequent_indent=continuation_indent,
        break_long_words=True,
        break_on_hyphens=False,
    )
    print("\n".join(lines))


def _pad_cell(value: str, width: int) -> str:
    return value + " " * max(0, width - _display_width(value))


def print_banner():
    width = _terminal_width()
    print("=" * width)
    _print_wrapped("MÔ PHỎNG ĐIỀU PHỐI THANG MÁY THÔNG MINH (CSD203 - FA26)", " ")
    _print_wrapped("12 tầng (1-12) | 10 khoang thang máy", " ")
    print("=" * width)


def _parse_integer(value: str, description: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{description} phải là số nguyên: '{value}'.") from None


def parse_elevators_input(line: str) -> List[Elevator]:
    """
    Parses a space-separated string of 10 elevator descriptors.
    Example: '1 3 5:10 8:2 4 6 7 9 11 12'
    """
    tokens = [t.lstrip('\ufeff').strip() for t in line.strip().split() if t.strip()]
    if len(tokens) != TOTAL_ELEVATORS:
        raise ValueError(f"Cần nhập đúng {TOTAL_ELEVATORS} trạng thái thang máy, hiện có {len(tokens)}.")

    elevators = []
    for idx, token in enumerate(tokens, start=1):
        if ":" in token:
            parts = token.split(":")
            if len(parts) != 2:
                raise ValueError(f"Định dạng '{token}' của thang #{idx} không hợp lệ. Cần nhập <tầng>:<tầng_đích>.")
            init_floor = _parse_integer(parts[0], f"Tầng hiện tại của thang #{idx}")
            dest_floor = _parse_integer(parts[1], f"Tầng đích của thang #{idx}")
            if not (1 <= init_floor <= TOTAL_FLOORS) or not (1 <= dest_floor <= TOTAL_FLOORS):
                raise ValueError(f"Tầng của thang #{idx} phải nằm trong khoảng [1..{TOTAL_FLOORS}]: '{token}'.")
            if init_floor == dest_floor:
                raise ValueError(
                    f"Tầng đích của thang #{idx} không thể trùng tầng hiện tại: '{token}'. "
                    f"Dùng '{init_floor}' để khai báo thang đứng yên."
                )
            elevators.append(Elevator(idx, init_floor, dest_floor))
        else:
            init_floor = _parse_integer(token, f"Tầng hiện tại của thang #{idx}")
            if not (1 <= init_floor <= TOTAL_FLOORS):
                raise ValueError(f"Tầng của thang #{idx} phải nằm trong khoảng [1..{TOTAL_FLOORS}]: '{token}'.")
            elevators.append(Elevator(idx, init_floor, None))

    return elevators


def parse_external_requests(line: str) -> List[ExternalRequest]:
    """
    Parses external requests line: e.g., '5U 2D 8U 5D'
    """
    tokens = [t.lstrip('\ufeff').strip() for t in line.strip().split() if t.strip()]
    requests = []
    for token in tokens:
        match = re.match(r"^(\d+)([UDud])$", token)
        if not match:
            raise ValueError(f"Yêu cầu gọi tầng ngoài '{token}' không hợp lệ. Cần nhập <tầng><U|D> (ví dụ: 5U, 2D).")
        floor = int(match.group(1))
        dir_char = match.group(2).upper()
        if not (1 <= floor <= TOTAL_FLOORS):
            raise ValueError(f"Tầng gọi {floor} phải nằm trong khoảng [1..{TOTAL_FLOORS}].")
        if floor == 1 and dir_char == "D":
            raise ValueError("Tầng 1 không thể gọi thang đi xuống.")
        if floor == TOTAL_FLOORS and dir_char == "U":
            raise ValueError(f"Tầng trên cùng {TOTAL_FLOORS} không thể gọi thang đi lên.")

        direction = Direction.UP if dir_char == "U" else Direction.DOWN
        requests.append(ExternalRequest(floor, direction))
    return requests


def parse_cabin_requests(line: str) -> List[CabinRequest]:
    """
    Parses cabin requests line: e.g., '1:10 1:3 3:1 2:12'
    """
    tokens = [t.lstrip('\ufeff').strip() for t in line.strip().split() if t.strip()]
    requests = []
    for token in tokens:
        parts = token.split(":")
        if len(parts) != 2:
            raise ValueError(f"Yêu cầu trong cabin '{token}' không hợp lệ. Cần nhập <mã_thang>:<tầng_đích> (ví dụ: 1:10).")
        elev_id = _parse_integer(parts[0], "Mã thang máy")
        target_floor = _parse_integer(parts[1], "Tầng đích")
        if not (1 <= elev_id <= TOTAL_ELEVATORS):
            raise ValueError(f"Mã thang máy {elev_id} phải nằm trong khoảng [1..{TOTAL_ELEVATORS}].")
        if not (1 <= target_floor <= TOTAL_FLOORS):
            raise ValueError(f"Tầng đích trong cabin {target_floor} phải nằm trong khoảng [1..{TOTAL_FLOORS}].")
        requests.append(CabinRequest(elev_id, target_floor))
    return requests


def display_results(elevators: List[Elevator], logs: List[str]):
    width = _terminal_width()
    print("\n" + "=" * width)
    _print_wrapped("NHẬT KÝ ĐIỀU PHỐI", " ")
    print("=" * width)
    if logs:
        for log in logs:
            _print_wrapped(f" [NHẬT KÝ] {log}", "           ")
    else:
        _print_wrapped(" (Không có yêu cầu gọi tầng ngoài hoặc yêu cầu trong cabin)")

    # 1. Trích xuất lộ trình hoàn chỉnh đã được tính toán bởi thuật toán LOOK
    routes = {elev.id: elev.generate_route() for elev in elevators}
    max_steps = max((len(r) - 1 for r in routes.values()), default=0)

    # 2. Hiển thị toàn bộ các điểm dừng trong một bảng gọn.
    if max_steps > 0:
        print("\n" + "=" * width)
        _print_wrapped("BẢNG CÁC BƯỚC DI CHUYỂN CỦA THANG MÁY", " ")
        print("=" * width)

        headers = ["Thang", "Vị trí đầu"] + [f"Đích {step}" for step in range(1, max_steps + 1)]
        rows = []
        for elev in elevators:
            route = routes[elev.id]
            destinations = [
                f"{'↑' if target > current else '↓'} {target}"
                for current, target in zip(route, route[1:])
            ]
            rows.append(
                [f"#{elev.id}", str(route[0])]
                + destinations
                + ["-"] * (max_steps - len(route) + 1)
            )
            for floor in route[1:]:
                elev.current_floor = floor

        column_widths = [
            max(_display_width(header), *(_display_width(row[index]) for row in rows))
            for index, header in enumerate(headers)
        ]
        fixed_indices = [0, 1]
        step_indices = list(range(2, len(headers)))
        fixed_width = sum(column_widths[index] for index in fixed_indices) + 3

        if step_indices and fixed_width + column_widths[step_indices[0]] + 3 > width:
            for row in rows:
                stops = " -> ".join(value for value in row[2:] if value != "-") or "không có"
                _print_wrapped(f"Thang {row[0]} | Tầng đầu: {row[1]} | Các điểm dừng: {stops}")
        else:
            groups = []
            group = []
            group_width = fixed_width
            for index in step_indices:
                added_width = column_widths[index] + 3
                if group and group_width + added_width > width:
                    groups.append(group)
                    group = []
                    group_width = fixed_width
                group.append(index)
                group_width += added_width
            if group:
                groups.append(group)
            if not groups:
                groups = [[]]

            for group_number, group_indices in enumerate(groups, start=1):
                if len(groups) > 1:
                    print(f"\nCác điểm dừng ({group_number}/{len(groups)}):")
                indices = fixed_indices + group_indices
                selected_widths = [column_widths[index] for index in indices]
                print(" | ".join(_pad_cell(headers[index], selected_widths[pos]) for pos, index in enumerate(indices)))
                print("-+-".join("-" * cell_width for cell_width in selected_widths))
                for row in rows:
                    print(" | ".join(
                        _pad_cell(row[index], selected_widths[pos])
                        for pos, index in enumerate(indices)
                    ))
    else:
        _print_wrapped("\n>> Tất cả 10 thang máy đều ở trạng thái đứng yên (Không có yêu cầu di chuyển).")

    for elev in elevators:
        elev.finish_route()


def read_initial_elevators() -> List[Elevator]:
    while True:
        try:
            _print_wrapped("[BƯỚC 1] Nhập trạng thái ban đầu của 10 thang máy (cách nhau bằng dấu cách):",
                           "         ")
            _print_wrapped("Định dạng: <tầng> nếu đứng yên, hoặc <tầng>:<tầng_đích> nếu đang di chuyển",
                           "         ")
            _print_wrapped("Ví dụ: 1 3 5:10 8:2 4 6 7 9 11 12", "         ")
            try:
                elev_line = input("Thang máy> ")
            except EOFError:
                print(">> Đã hết dữ liệu nhập. Sử dụng cấu hình mặc định.")
                elev_line = "1 3 5:10 8:2 4 6 7 9 11 12"

            if not elev_line.strip():
                print(">> Tự động sử dụng cấu hình mặc định.")
                elev_line = "1 3 5:10 8:2 4 6 7 9 11 12"
                print(f"Thang máy> {elev_line}")
            elevators = parse_elevators_input(elev_line)
            return elevators
        except (ValueError, IndexError) as e:
            _print_wrapped(f">> Lỗi: {e} Vui lòng nhập lại.")
            print()


def run_simulator():
    print_banner()
    elevators = read_initial_elevators()

    while True:
        # Bước 2: Yêu cầu gọi thang từ bên ngoài
        while True:
            try:
                _print_wrapped("\n[BƯỚC 2] Nhập yêu cầu gọi thang từ bên ngoài (cách nhau bằng dấu cách):",
                               "         ")
                _print_wrapped("Định dạng: <tầng><U|D>, trong đó U là đi lên, D là đi xuống", "         ")
                _print_wrapped("Ví dụ: 6U 3D 10D 6D (nhấn phím Enter nếu không có yêu cầu)", "         ")
                try:
                    ext_line = input("Gọi tầng> ")
                except EOFError:
                    ext_line = ""
                external_requests = parse_external_requests(ext_line)
                break
            except (ValueError, IndexError) as e:
                _print_wrapped(f">> Lỗi: {e} Vui lòng nhập lại.")
                print()

        # Bước 3: Yêu cầu chọn tầng trong cabin
        while True:
            try:
                _print_wrapped("\n[BƯỚC 3] Nhập yêu cầu chọn tầng bên trong thang máy (cách nhau bằng dấu cách):",
                               "         ")
                _print_wrapped("Định dạng: <mã_thang>:<tầng_đích>", "         ")
                _print_wrapped("Ví dụ: 1:12 3:1 4:1 (nhấn phím Enter nếu không có yêu cầu)", "         ")
                try:
                    cab_line = input("Chọn tầng> ")
                except EOFError:
                    cab_line = ""
                cabin_requests = parse_cabin_requests(cab_line)
                break
            except (ValueError, IndexError) as e:
                _print_wrapped(f">> Lỗi: {e} Vui lòng nhập lại.")
                print()

        # Feed into Direction-separated Queues per Topic 9 specification:
        # "Queue: Lưu danh sách yêu cầu đang chờ xử lý theo từng hướng."
        up_external_queue = FIFOQueue()
        down_external_queue = FIFOQueue()
        for req in external_requests:
            if req.direction == Direction.UP:
                up_external_queue.enqueue(req)
            else:
                down_external_queue.enqueue(req)

        dispatcher = GroupDispatcher(elevators, total_floors=TOTAL_FLOORS)
        logs = dispatcher.run_dispatch(up_external_queue, cabin_requests, down_queue=down_external_queue)
        display_results(elevators, logs)

        _print_wrapped("Chọn lượt tiếp theo:")
        _print_wrapped("1. Giữ nguyên vị trí hiện tại của các thang và nhập yêu cầu mới", "   ")
        _print_wrapped("2. Đặt lại toàn bộ thang và nhập trạng thái ban đầu mới", "   ")
        while True:
            try:
                choice = input("Lựa chọn (1/2): ").strip()
            except EOFError:
                print("\n>> Đã hết dữ liệu nhập. Kết thúc chương trình.")
                return

            if choice == "1":
                break
            if choice == "2":
                elevators = read_initial_elevators()
                break
            _print_wrapped(">> Lựa chọn không hợp lệ. Vui lòng nhập 1 hoặc 2.")
            print()


if __name__ == "__main__":
    run_simulator()
