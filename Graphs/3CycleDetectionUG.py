from collections import deque


def  isCycleBfs(node, graph, visited):

    q.append((node,-1))
    visited[node] = 1

    while q:
        a = q.popleft()

        for i in graph[a[0]]:
            if not visited[i]:
                q.append((i,a[0]))
                visited[i] = 1
            elif i!=a[1]:
                return True
    return False

def isCycleDfs(node, graph, visited, parent):
    
    visited[node] = 1


    for i in graph[node]:
        if not visited[i]:
            if isCycleDfs(i, graph, visited, node):
                return True
        elif i!=parent:
            return True
    return False
    

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
q = deque()
for i in graph:
    if not visited[i]:
        if isCycleDfs(i, graph, visited, -1):
            print(True)
            break
print(False)

