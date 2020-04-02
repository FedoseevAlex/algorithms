from typing import List


def sift_up(heap: List, pos: int = None):
    if pos is None:
        pos = len(heap) - 1
    current, parent = pos, (pos - 1) // 2

    while current > 0:
        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
        else:
            break
        current, parent = parent, (parent - 1) // 2


def sift_down(heap: List, pos: int = 0):
    while pos < len(heap):
        left = pos * 2 + 1
        right = pos * 2 + 2
        if right < len(heap):
            max_child = left if heap[left] > heap[right] else right
        elif left < len(heap):
            max_child = left
        else:
            return

        if heap[pos] < heap[max_child]:
            heap[pos], heap[max_child] = heap[max_child], heap[pos]

        pos = max_child


def insert(heap: List, number: int):
    heap.append(number)
    sift_up(heap, len(heap) - 1)


def heapify(array: List):
    for idx in range(len(array), -1, -1):
        sift_down(array, idx)


def pop(heap: List):
    root = heap[0]
    if heap:
        heap[0] = heap[-1]
        heap.pop()
        sift_down(heap)
    return root


def make_answer(ops):
    heap = list()
    for op in ops:
        op = op.split()
        if len(op) > 1:
            insert(heap, int(op[1]))
        else:
            yield(pop(heap))


if __name__ == "__main__":
    pass
