"""
Custom Data Structures for Smart Elevator Dispatch Simulator.
CSD203 - Data Structures and Algorithms (FA26)
Zero external dependencies: Fully self-implemented Heap and Queue.
"""

class MinHeap:
    """Min-Heap implementation for ordering UP elevator stops in ascending order."""
    def __init__(self):
        self._data = []

    def insert(self, val: int) -> None:
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)

    def extract_min(self) -> int:
        if self.is_empty():
            raise IndexError("extract_min from empty heap")
        min_val = self._data[0]
        last_val = self._data.pop()
        if self._data:
            self._data[0] = last_val
            self._heapify_down(0)
        return min_val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def contains(self, val: int) -> bool:
        return val in self._data

    def copy(self) -> "MinHeap":
        h = MinHeap()
        h._data = list(self._data)
        return h

    def __len__(self) -> int:
        return len(self._data)

    def _heapify_up(self, idx: int) -> None:
        parent = (idx - 1) // 2
        while idx > 0 and self._data[idx] < self._data[parent]:
            self._data[idx], self._data[parent] = self._data[parent], self._data[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _heapify_down(self, idx: int) -> None:
        size = len(self._data)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest != idx:
                self._data[idx], self._data[smallest] = self._data[smallest], self._data[idx]
                idx = smallest
            else:
                break


class MaxHeap:
    """Max-Heap implementation for ordering DOWN elevator stops in descending order."""
    def __init__(self):
        self._data = []

    def insert(self, val: int) -> None:
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)

    def extract_max(self) -> int:
        if self.is_empty():
            raise IndexError("extract_max from empty heap")
        max_val = self._data[0]
        last_val = self._data.pop()
        if self._data:
            self._data[0] = last_val
            self._heapify_down(0)
        return max_val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def contains(self, val: int) -> bool:
        return val in self._data

    def copy(self) -> "MaxHeap":
        h = MaxHeap()
        h._data = list(self._data)
        return h

    def __len__(self) -> int:
        return len(self._data)

    def _heapify_up(self, idx: int) -> None:
        parent = (idx - 1) // 2
        while idx > 0 and self._data[idx] > self._data[parent]:
            self._data[idx], self._data[parent] = self._data[parent], self._data[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _heapify_down(self, idx: int) -> None:
        size = len(self._data)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < size and self._data[left] > self._data[largest]:
                largest = left
            if right < size and self._data[right] > self._data[largest]:
                largest = right

            if largest != idx:
                self._data[idx], self._data[largest] = self._data[largest], self._data[idx]
                idx = largest
            else:
                break


class FIFOQueue:
    """FIFO Queue implementation for processing external hall requests."""
    def __init__(self):
        self._items = []
        self._head = 0

    def enqueue(self, item) -> None:
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items[self._head]
        self._head += 1
        # Compact list if head exceeds threshold to avoid memory leaks
        if self._head > 50 and self._head > len(self._items) // 2:
            self._items = self._items[self._head:]
            self._head = 0
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[self._head]

    def is_empty(self) -> bool:
        return self._head >= len(self._items)

    def __len__(self) -> int:
        return len(self._items) - self._head
