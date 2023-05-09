from copy import copy
from typing import List, Tuple
from solution import solve
import random

        
        
def backtrack(graph, path, u, v, l):
    useful_edges = set()

    if u == v and l >= 0:
        useful_edges = set(copy(path))

    if l < 0:
        return set()

    for z, w in graph[u]:
        if (u,z) not in path:
            for x,y in backtrack(graph, path + [(u, z)], z, v, l-w):
                useful_edges.add((x,y))

    return useful_edges

# brute force
def solve2(n : int, edges : List[Tuple[int,int,int]], Q : List[Tuple[int,int,int]]):    
    useful_edges = set()
    
    G = [[] for _ in range(n)]
    for x,y,w in edges:
        G[x].append((y, w))
        G[y].append((x, w))

    for u, v, l in Q:
        for u1, v1 in backtrack(G, [], u, v, l):
            if not useful_edges.__contains__((u1, v1)) and \
                not useful_edges.__contains__((v1, u1)):
                useful_edges.add((u1, v1))

    return useful_edges


    
        
def random_graph(n, prob):
    _edges = set()
    edges = []
    
    for i in range(n):
        for j in range(n):
            if random.random() < prob and i != j and not _edges.__contains__((j,i)):
                _edges.add((i,j))
                edges.append((i,j, random.randint(0,500)))
                
    return edges


def tester(amount_tests: int, max_nodes: int):
    
    for case in range(amount_tests):
        
        n = random.randint(1, max_nodes)
        
        edges = random_graph(n, 0.5) #TODO: adjust p value
        
        Q = random_graph(n, 0.2) #TODO: adjust p value

        k1 = solve(n, edges, Q)
        print('START TESTER')
        print(f'EDGES: {edges}')
        print(f'Q: {Q}')
        k2 = solve2(n ,edges, Q)
        
        print("\033[1;37m" + f'Test Case {case}, verdict:')
        if k1 == len(k2):
            print(chr(27) + "[1;32m" + "Accepted")
        else:
            print(chr(27) + "[1;31m" +'Wrong Answer')
            print(f'ANSWER => sol: {k1} test: {len(k2)}')
            print(f'TESTER: {k2}')
        print("\033[0;37m" )


if __name__ == '__main__':
    AMOUNT_OF_TEST_CASES = 100
    MAX_NUMBER_OF_NODES = 8

    tester(
        amount_tests=AMOUNT_OF_TEST_CASES,
        max_nodes=MAX_NUMBER_OF_NODES
    )

    # EDGES = [(0, 2, 138), (0, 3, 291), (0, 4, 35), (1, 2, 128), (1, 4, 477), (3, 1, 94)]
    # Q = [(1, 3, 310), (2, 0, 303), (3, 0, 194)]

    # # dead case
    # EDGES = [(1, 0, 338), (1, 2, 457), (1, 4, 41), (2, 0, 299), (2, 4, 20), (3, 1, 1), (3, 2, 461), (3, 6, 417), (5, 2, 168), (5, 3, 60), (6, 0, 228), (6, 5, 249)]
    # Q = [(1, 0, 326), (1, 2, 225), (3, 1, 295), (5, 2, 146), (6, 3, 422)]

    # EDGES = [(0, 2, 91), (1, 2, 288), (1, 4, 67), (2, 3, 9), (2, 4, 46), (3, 0, 85), (4, 0, 189), (4, 3, 67)]
    # Q = [(1, 3, 217), (2, 3, 21), (4, 2, 359)]

    # print(solve2(5, EDGES, Q))

 
