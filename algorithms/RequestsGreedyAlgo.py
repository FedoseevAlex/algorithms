"""
Greedy Algorithm to find maximum non-overlapping line segments
"""
from typing import List, Tuple


def find_requests(segments: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Implementation of greedy algorithm for requests task
    """
    segments = sorted(segments, key=lambda seg: seg[1])
    result = [segments[0]]
    for segment in segments[1:]:
        if segment[0] > result[-1][1]:
            result.append(segment)

    return result

if __name__ == "__main__":
    seg_num = int(input())
    segments = list()
    for seg in range(seg_num):
        segments.append(tuple(map(int, input().strip().split())))

    requests = find_requests(segments)
    print(requests)



