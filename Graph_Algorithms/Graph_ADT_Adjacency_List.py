class Graph:
    # Constructor
    def __init__(self):
        # dictionary to store graph
        self.graph = {}

    # function to add an edge to graph
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        visited = set()
        visited.add(start)
        queue = [start]
        res = []
        while queue:
            root = queue.pop(0)
            res.append(root)
            for node in self.graph[root]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return res

    def dfs(self, start):
        visited = set()
        visited.add(start)
        queue = [start]
        res = []
        while queue:
            root = queue.pop()
            res.append(root)
            for node in self.graph[root]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return res


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    bfs = g.bfs(2)
    assert bfs == [2, 0, 3, 1]
    dfs = g.dfs(2)
    assert dfs == [2, 3, 0, 1]
