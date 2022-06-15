from collections import deque

def isCycleDfs(node, graph, visited, currVisited):

    visited[node] = 1
    currVisited[node] = 1

    for i in graph[node]:
        if not visited[i]:
            if isCycleDfs(i, graph, visited, currVisited):
                return True

        elif currVisited[i]:
            return True

    currVisited[node] = 0
    return False

# Using bfs(Kahn's Algo) - So topo sort can be created for only directed acyclic graph
# so here we will try to produce topo sort and if we are sucessful then there is no 
# cycle else there is cycle.
# To do so we will have a count and if that count at the end becomes equal to 
# number of nodes in a graph(because topo sort will have same number of nodes as in graph)
# the there is no cycle else there is a cycle.

def isCycleBfs(graph, n):
    indegree = [0]*(n+1)
    q  = deque()

    for i in graph:
        for j in graph[i]:
            indegree[j] += 1
    
    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    c = 0
    while q:
        a = q.popleft()
        c+=1

        for i in graph[a]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if c == n:
        return False
    return True

n = 9
graph = {
    1:[2],
    2:[3],
    3:[4,6],
    4:[5],
    5:[],
    6:[5],
    7:[2,8],
    8:[9],
    9:[7]
}        

visited = [0]*(n+1)
currVisited = [0]*(n+1)

for i in graph:
    if not visited[i]:
        if isCycleDfs(i, graph, visited, currVisited):
            print("true from dfs")

if isCycleBfs(graph, n):
    print("true from bfs")
