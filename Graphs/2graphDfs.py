def dfs(node, graph, visited):

    visited[node] = 1
    print(node)

    for i in graph[node]:
        if not visited[i]:
            dfs(i,graph, visited)


n = 7
graph = {
    0:[1],
    1:[0,2,6],
    2:[1,4],
    3:[5],
    4:[2,6],
    5:[3],
    6:[1,4]
}

visited = [0]*n

for i in graph:
    if not visited[i]:
        dfs(i,graph, visited)
   