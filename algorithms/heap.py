from typing import List


def sift_up(heap: List):
    bubble = len(heap) - 1
    parent = bubble // 2
    while bubble > 0:
        if heap[bubble] > heap[parent]:
            heap[bubble], heap[parent] = heap[parent], heap[bubble]
        parent, bubble = parent // 2, parent


def insert(heap: List, number: int):
    heap.append(number)
    sift_up(heap)


def sift_down(heap: List):
    bubble = 0
    left, right = bubble * 2 + 1, bubble * 2 + 2

    while bubble < len(heap):
        if right < len(heap):
            max_child = left if heap[left] > heap[right] else right
        elif left < len(heap):
            max_child = left
        else:
            break

        if heap[max_child] > heap[bubble]:
            heap[max_child], heap[bubble] = heap[bubble], heap[max_child]
        bubble, left, right = max_child, max_child * 2 + 1, max_child * 2 + 2


def pop_max(heap: List) -> int:
    root = heap.pop(0) if heap else None
    if heap:
        heap.append(heap.pop())
        sift_down(heap)
    return root


if __name__ == "__main__":
    ops_num = int(input())
    ops = list()
    for _ in range(ops_num):
        ops.append(input().split())

    arr = list()
    for op in ops:
        if len(op) > 1:
            insert(arr, int(op[1]))
        else:
            print(pop_max(arr))
