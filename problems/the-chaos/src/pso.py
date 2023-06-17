
import numpy as np
from random import uniform, random
from copy import deepcopy
from typing import List
from graph import Graph


class Particle:
    def __init__(self, graph: Graph, x0: Graph, k: int):
        self.graph = deepcopy(graph)
        self.k = k

        self.position = deepcopy(x0)
        self.velocity=[]            # particle velocity
        self.best=None              # best individual position
        self.err_best=-1            # best individual error
        self.err=-1                 # individual error

        for i in range(0, graph.N):
            self.velocity.append(uniform(-1,1))

    # evaluate current fitness
    def evaluate(self):
        k = 0
        degree_3 = 0

        for i in range(self.position.N):
            degree = len(self.position[i+1])
            if degree > 0:
                k += 1
            if degree == 3:
                degree_3 += 1

        self.err = degree_3
        
        if k != self.k:
            self.err = 0.9 ** abs(k-self.k) * degree_3

        # check to see if the current position is an individual best
        if self.err > self.err_best or self.err_best == -1:
            self.best = deepcopy(self.position)
            self.err_best = self.err

    # update new particle velocity
    def update_velocity(self, swarm_best: list):
        w=0.9       # constant inertia weight (how much to weight the previous velocity)
        c1=4        # cognative constant
        c2=6        # social constant

        for i in range(0, self.graph.N):
            r1=random()
            r2=random()

            cognitive_force = c1*r1*(len(self.best[i+1]) - len(self.position[i+1]))
            social_force = c2*r2*(len(swarm_best[i+1]) - len(self.position[i+1]))

            self.velocity[i] = w*self.velocity[i] + cognitive_force + social_force

    # update the particle position based off new velocity updates
    def update_position(self):
        new_pos = []

        for i in range(0, self.graph.N):
            new_pos.append(len(self.position[i+1]) + self.velocity[i])

        for i in range(0, self.graph.N):
            if abs(new_pos[i] - len(self.position[i+1])) > 1:
                new_pos[i] = int(new_pos[i] - len(self.position[i+1]))
            else:
                new_pos[i] = 0

        incr = [i+1 for i, v in enumerate(new_pos) if v > 0]
        decr = [i+1 for i, v in enumerate(new_pos) if v < 0]

        for v in incr:
            edges = [u for u in self.graph[v] if not u in self.position[v]]
            weights = [u+1 for i, u in enumerate(new_pos) if u > 0 and i+1 in self.graph[v] and not i+1 in self.position[v]]
            sum_weights = sum(weights)
            weights = [w/sum_weights for w in weights]
            
            if len(edges) == len(weights) and len(edges) > 0:
                e = np.random.choice(edges, p=weights)
                self.position.AddEdge((e, v))

        for v in decr:
            edges = [u for u in self.graph[v] if u in self.position[v]]
            weights = [abs(u) + 1 for i, u in enumerate(new_pos) if u < 0 and i+1 in self.graph[v] and i+1 in self.position[v]]
            sum_weights = sum(weights)
            weights = [w/sum_weights for w in weights]

            if len(edges) == len(weights) and len(edges) > 0:
                e = np.random.choice(edges, p=weights)
                self.position.RemoveEdge((e, v))


def maximize(swarm: List[Particle], max_iter, verbose=False):

    err_best=-1              # best error for group
    swarm_best=[]            # best position for group

    # begin optimization loop
    i=0
    while i < max_iter:
        if verbose: print(f'iter: {i:>4d}, best solution: {err_best:10.6f}')
            
        # cycle through particles in swarm and evaluate fitness
        for j in range(0, len(swarm)):
            swarm[j].evaluate()

            # determine if current particle is the best (globally)
            if swarm[j].err > err_best or err_best == -1:
                swarm_best = deepcopy(swarm[j].position)
                err_best = float(swarm[j].err)
        
        # cycle through swarm and update velocities and position
        for j in range(0, len(swarm)):
            swarm[j].update_velocity(swarm_best)
            swarm[j].update_position()
        i+=1

    # print final results
    if verbose:
        print('\nFINAL SOLUTION:')
        print(f'   > {swarm_best}')
        print(f'   > {err_best}\n')

    return err_best, swarm_best
