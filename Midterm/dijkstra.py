import heapq

def dijkstra_shortest_path(graph, start, goal):
    dist = {node: float("inf") for node in graph}
    parent = {start: None}
    dist[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        if u == goal:
            break

        for v, w in graph[u]:
            if v in visited:
                continue
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    if dist.get(goal, float("inf")) == float("inf"):
        return None, float("inf")

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return path, dist[goal]
