from particle import *
from vector import *

class Simulation:

    def __init__(self, particles, gravity, width, height, dt, substeps):
        self.particles = particles
        self.width = width
        self.height = height
        self.dt = dt/substeps
        self.substeps = substeps
        self.g = gravity

    def time_step(self):
        i = 0

        while(i < self.substeps):
            for j in range(len(self.particles)):
                for k in range(j, len(self.particles)):
                    if(circles_collision(self.particles[j], self.particles[k])):
                        circles_scatter(self.particles[j], self.particles[k])
            i+=1

        self.apply_gravity()

    def draw()

    def apply_gravity(self):
        for j in range(len(self.particles)):
            self.particles.apply_force(self.particles[j].getMass()*self.g, self.dt*self.substeps)
        