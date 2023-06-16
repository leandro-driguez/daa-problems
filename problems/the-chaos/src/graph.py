from copy import deepcopy
from random import randint
from typing import Tuple


class Graph:    
    def __init__(self, N, e: dict[int, set] = None):
        self.N = N
        
        if e is None:
            e = { i+1:set() for i in range(N) }
        
        self.e = deepcopy(e)

    def __getitem__(self, v: int):
        if not isinstance(v, int):
            raise Exception("")
        return self.e[v]
    
    def AddEdge(self, e: Tuple[int, int]):
        u, v = e
        
        if u != v and not v in self.e[u] and not u in self.e[v]:
            self.e[u].add(v)
            self.e[v].add(u)
            return True

        return False
    
    def RemoveEdge(self, e: Tuple[int, int]):
        u, v = e

        if u != v and v in self.e[u] and u in self.e[v]:
            self.e[u].remove(v)
            self.e[v].remove(u)
            return True

        return False

    def Subgraph(self, v: set()):
        subgraph = Graph(self.N)

        for u in v:
            for w in self[u]:
                if w in v:
                    subgraph.AddEdge((u,w))

        return subgraph

    @staticmethod
    def Generate(N: int):
        M = randint(0, N * (N-1) / 2)
        graph = Graph(N)

        for _ in range(M):
            u = v = 1

            while not graph.AddEdge((u,v)):
                u = randint(1, N)
                v = randint(1, N)

        return graph

if __name__ == '__main__':
    
    graph = Graph.Generate(4)
    print(graph.e)
    subgraph = graph.Subgraph([1, 2, 3])
    
    