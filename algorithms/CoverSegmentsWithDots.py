"""
Solution for stepik task
https://stepik.org/lesson/13238/step/9?auth=login&unit=3424
"""


def find_points(segments):
    segments = sorted(segments, key=lambda seg: seg[1])
    result = [segments[0][1]]

    for segment in segments[1:]:
        if result[-1] < segment[0]:
            result.append(segment[1])
    return result


if __name__ == "__main__":
    seg_num = int(input())

    segments = list()
    for _ in range(seg_num):
        segments.append(tuple(map(int, input().strip().split())))

    result = find_points(segments)

    print(len(result))
    print(*result)

