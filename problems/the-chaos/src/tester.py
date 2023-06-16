from typing import List, Tuple


def combinations(n: list, m: int, comb: list = [], index: int = 0):
    if len(comb) == m:
        return [comb]

    combs = []

    for i in range(index, len(n)):
        combs.extend(combinations(n, m, comb + [n[i]], i + 1))

    return combs


def k_regular(edges: List[Tuple[int, int]], k: int):
    degree = dict()

    for u, v in edges:
        try:
            degree[u]+=1
        except KeyError:
            degree[u]=1

        try:
            degree[v]+=1
        except KeyError:
            degree[v]=1

    for _, v in degree.items():
        if v != k:
            return False

    return True


def solve(edges: List[Tuple[int, int]], amount_nodes: int, k: int):

    for v in range(2, amount_nodes + 1):
        for subgraph in combinations(edges, 3*v/2):
            if k_regular(subgraph, k):
                return subgraph

    return []


if __name__ == '__main__':

    edges =[
        (0, 1),
        (0, 3),
        (0, 5),
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 5),
        (3, 4),
        (4, 5),
    ]

    subgraph=solve(edges, 6, 3)
    
    print(subgraph)
