import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)]
}

heuristic = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        if g != best_cost.get(node):
            continue

        for neighbor, weight in graph[node]:
            new_cost = g + weight

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (priority, new_cost, neighbor,
                     path + [neighbor])
                )

    return None, float("inf")

path, cost = astar("A", "D")

print("A* Algorithm")
print("Shortest path:", " -> ".join(path))
print("Total cost:", cost)
