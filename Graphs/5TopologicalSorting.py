# Topo Sort using DFS
# Topo sort is possible for only Directed Acyclic Graph

from collections import deque


def topoDfs(node, visited, stack):

    visited[node] = 1

    for i in graph[node]:
        if not visited[i]:
            topoDfs(i, visited, stack)

    stack.append(node)

#Using BFS -  Kahn's Algo

def topoBfs(graph,n):
    indegree = [0]*n
    q = deque()
    topo = []

    for i in graph:
        for j in graph[i]:
            indegree[j]+=1
    
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        a = q.popleft()
        topo.append(a)

        for i in graph[a]:
            indegree[i]-=1

            if indegree[i] == 0:
                q.append(i)

    print(topo)


n = 6
graph = {
    0:[],
    1:[],
    2:[3],
    3:[1],
    4:[0,1],
    5:[0,2],
    
}     

visited = [0]*(n+1)
stack = []

for i in graph:
    if not visited[i]:
        topoDfs(i, visited, stack)

print(stack) # stack will have reverse order of topo sort, pop elements on by one and u will get topo sort in correct order



topoBfs(graph, n)
