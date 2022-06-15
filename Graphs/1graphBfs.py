import collections

def bfs(src, graph, visited):

    q = collections.deque()

    q.append(src)
    visited[src] = 1

    while q:
        a = q.popleft()
        print(a)
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

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
        bfs(i,graph, visited)
   