def dfs(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
