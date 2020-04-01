from typing import List


def sift_up(heap: List, pos: int = None):
    if pos is None:
        pos = len(heap) - 1
    current, parent = pos, pos // 2

    while current > 0:
        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
        else:
            break
        current, parent = parent, parent // 2


def sift_down(heap: List, pos: int = 0):
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

    sift_down(heap, max_child)


def insert(heap: List, number: int):
    heap.append(number)
    sift_up(heap, len(heap) - 1)


def heapify(array: List):

    for idx in reversed(range(len(array))):
        sift_down(array, idx)


def pop(heap: List):
    root = heap.pop(0)
    if heap:
        heap.insert(0, heap.pop())
        sift_down(heap)
    return root


if __name__ == "__main__":
    pass
