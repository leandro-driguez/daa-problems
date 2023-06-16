
import random
from graph import Graph
import numpy as np

class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.best_position = position
        self.best_error = np.inf

def objective_function(position):
    return np.sum(position ** 2)

def update_velocity(particle, global_best_position, w, c1, c2):
    r1, r2 = random.random(), random.random()
    cognitive = c1 * r1 * (particle.best_position - particle.position)
    social = c2 * r2 * (global_best_position - particle.position)
    particle.velocity = w * particle.velocity + cognitive + social

def update_position(particle):
    particle.position += particle.velocity

def pso(n_particles, n_epochs, search_space, w, c1, c2):
    particles = [Particle(np.random.uniform(search_space[0], search_space[1]), np.random.uniform(-1, 1)) for _ in range(n_particles)]
    global_best_position = None
    global_best_error = np.inf

    for epoch in range(n_epochs):
        for particle in particles:
            error = objective_function(particle.position)
            if error < particle.best_error:
                particle.best_position = particle.position
                particle.best_error = error

            if error < global_best_error:
                global_best_position = particle.position
                global_best_error = error

            update_velocity(particle, global_best_position, w, c1, c2)
            update_position(particle)

    return global_best_position

if __name__ == '__main__':
    n_particles = 50
    n_epochs = 1000
    search_space = (-5, 5)
    w = 0.7
    c1 = 2
    c2 = 2

    best_position = pso(n_particles, n_epochs, search_space, w, c1, c2)
    print("Best position found:", best_position)
    
    l = 10*[1] + 20*[0]
    random.shuffle(l)
    print(l)
    
    # Graph.Generate(10)
    
