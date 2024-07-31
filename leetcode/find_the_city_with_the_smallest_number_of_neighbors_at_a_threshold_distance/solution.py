"""
There are n cities numbered from 0 to n-1.
Given the array edges where edges[i] = [from_i, to_i, weight_i] represents a bidirectional and weighted edge between cities
from_i and to_i, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and
whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
"""
from typing import List

import heapq

def Dijkstra(n: int, edges: List[List[int]], distanceThreshold: int) -> int | float:
    distances_map = {}
    for f, t, w in edges:
        f_map = distances_map.setdefault(f, {})
        f_map[t] = w
        t_map = distances_map.setdefault(t, {})
        t_map[f] = w

    shortest_distances = {}
    for source in range(n):
        shortest_distances[source] = _dijkstra(source, distances_map)

    answer: int | float = -float('inf')
    least_cities = float('inf')
    for source, distances in shortest_distances.items():
        reachable_cities = sum(0 < distance <= distanceThreshold for distance in distances.values())
        if reachable_cities <= least_cities and source > answer:
            answer = source
            least_cities = reachable_cities

    return answer

def _dijkstra(source: int, distances_map: dict[int, dict[int, int]]) -> dict[int, int | float]:
    shortest_distances: dict[int, int | float] = {source: 0}
    shortest_distances.update(distances_map.get(source, {}))

    queue: List[tuple[int | float, int]] = [(weight, node) for node, weight in shortest_distances.items()]
    heapq.heapify(queue)

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if shortest_distances.get(current_node, float('inf')) < current_distance:
            continue

        for neighbor, neighbor_distance in distances_map.get(current_node, {}).items():
            new_distance = current_distance + neighbor_distance
            if new_distance < shortest_distances.get(neighbor, float('inf')):
                shortest_distances[neighbor] = new_distance
                heapq.heappush(queue, (shortest_distances.get(neighbor, float('inf')), neighbor))
    return shortest_distances


def WFI(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # distance matrix
    m = [[float('Inf') if i != j else 0 for i in range(n)] for j in range(n)]
    for f, t, w in edges:
        m[f][t], m[t][f] = w, w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                m[i][j] = min(m[i][j], m[i][k] + m[k][j])
    answer = n
    lowest_cities = n
    for idx, row in enumerate(m):
        cities = sum(0 < i <= distanceThreshold for i in row)
        if cities <= lowest_cities:
            answer = idx
            lowest_cities = cities
    return answer

if __name__ == "__main__":
    # test case is a tuple
    # n, edges, distanceThreshold, expected_answer
    test_cases = [
        (4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4, 3),
        (5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2, 0)
    ]
    for test_case_num, (n, edges, distanceThreshold, expected_answer) in enumerate(test_cases):
        assert WFI(n, edges, distanceThreshold) == expected_answer, f"wfi gave wrong answer for test case №{test_case_num}"
        assert Dijkstra(n, edges, distanceThreshold) == expected_answer, f"dijkstra gave wrong answer for test case №{test_case_num}"
    print("All test cases are passed!")
