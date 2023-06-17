
from typing import List
from graph import Graph
from pso import Particle, maximize
from random import shuffle
from tester import solve


def gen_particles(graph: Graph, k: int, amount_particles: int):
    particles: List[Particle] = []

    v = k * [1] + (graph.N - k) * [0]
    
    for _ in range(amount_particles):
        shuffle(v)

        v_subgraph = [i+1 for i, v in enumerate(v) if v != 0]
        x0 = graph.Subgraph(v_subgraph)

        particles.append(Particle(graph, x0, k))

    return particles


if __name__ == '__main__':
    N = 10

    graph = Graph.Generate(N)

    for k in range(4, N+1):
        swarm = gen_particles(graph, k, 100)

        best, _ = maximize(swarm, 50, False)

        edges = set()

        for u in range(1, N+1):
            for v in graph[u]:
                if not (u,v) in edges and not (v,u) in edges:
                    edges.add((u,v))

        print(f'\nK: {k} => {best}\n{solve(list(edges), N, k)}\n')
        