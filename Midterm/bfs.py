from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        u = queue.popleft()

        if u == goal:
            break

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

    if goal not in parent:
        return None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path
