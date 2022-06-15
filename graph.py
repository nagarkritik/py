from collections import defaultdict
from collections import deque
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def insert(self,st,end):
        self.graph[st].append(end)

    def print(self):
        print(self.graph)

    def BFS(self,s):
        visit = {s:1}

        q = deque([s])

        while q:
            p = q.popleft()
            print(p, end=" ")
            for i in self.graph[p]:
                if i not in visit:
                    visit[i] = 1
                    q.append(i)

    def DFS_help(self,node,visit):

        visit[node] = 1
        print(node, end=" ")
        for i in self.graph[node]:
            if i not in visit:
                self.DFS_help(i,visit)

    def DFS(self,st):
        visit = {}

        self.DFS_help(st,visit)


g = Graph()
g.insert(0,1)
g.insert(0,2)
g.insert(1,2)
g.insert(2,0)
g.insert(2,3)
g.insert(3,3)
g.print()
g.BFS(2)
print("")
g.DFS(2)

    


