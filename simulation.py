from particle import *
from vector import *
from wall import *

class Simulation:

    def __init__(self, particles, walls, width, height, gravity, dt, substeps):
        self.particles = particles
        self.width = width
        self.height = height
        self.dt = dt/substeps
        self.substeps = substeps
        self.g = gravity

        if len(walls != 0):
            self.walls = walls
        else:
            self.walls = [Wall("up", 0, 0), Wall("down", 0, 0), Wall("left", 0, 0), Wall("right", 0, 0)]

    def time_step(self):
        i = 0

        #colissions
        while(i < self.substeps):
            for j in range(len(self.particles)):


                for k in range(j, len(self.particles)):
                    if(circles_collision(self.particles[j], self.particles[k])):
                        circles_scatter(self.particles[j], self.particles[k])
            i+=1

        #self.apply_gravity()

    def draw(self, screen):

        #Добавить рисование поля

        for i in range(len(self.particles)):
            self.particles[i].draw(screen)

    def apply_gravity(self):
        for j in range(len(self.particles)):
            self.particles.apply_force(self.particles[j].getMass()*self.g, self.dt*self.substeps)

    def find_wall(self, side):
        
        for wall in self.walls:
            if side == wall.getSide():
                return wall
            
        return 0

    def wall_collision(self, particle):

        if particle.getPosition().X() - self.find_wall("left").getPosition() <= particle.getRadius():
            wall_scattering(particle, self.find_wall("left"))
        if particle.getPosition().X() - self.find_wall("right").getPosition() >= particle.getRadius():
            wall_scattering(particle, self.find_wall("right"))
        if particle.getPosition().Y() - self.find_wall("top").getPosition() <= particle.getRadius():
            wall_scattering(particle, self.find_wall("top"))
        if particle.getPosition().Y() - self.find_wall("bottom").getPosition() >= particle.getRadius():
            wall_scattering(particle, self.find_wall("bottom"))
        