from heapq import heappop, heappush
from collections import defaultdict
from re import split


def dijkstra(start, graph):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
    return [distances[node] for node in graph]


with open("rosalind_ba7a.txt") as f:
    lines = f.readlines()

n = int(lines[0])
lines.pop(0)
adjacency_list = defaultdict(list)
for line in lines:
    nums = split(r"\D+", line)
    adjacency_list[int(nums[0])].append((int(nums[1]), int(nums[2])))

for i in range(n):
    d = dijkstra(i, adjacency_list)
    for j in range(n):
        print(d[j], end=" ")
    print()