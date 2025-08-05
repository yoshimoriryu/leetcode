from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print(self.graph)

    def BFS(self, start, find):
        self.visited = []
        self.queue = []

        self.queue.append(start)

        while self.queue:
            curr = self.queue.pop(0)
            self.visited.append(curr)

            if curr == find:
                print(self.queue)
                print(self.visited)
                return curr
            for i in self.graph[curr]:
                if i not in self.visited:
                    self.queue.append(i)
        return "not found"


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3)
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
print(g.BFS(2,3))
g.printGraph()