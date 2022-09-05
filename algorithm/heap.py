"""Heap Algorithm
"""


class Heap:
    def __init__(self, seq: list[int] = [], min_heap: bool = True) -> None:
        self.seq = seq
        self.heap = seq
        self.size = len(seq)

    def heapfify(self):
        pass


if __name__ == "__main__":
    heap = Heap()
