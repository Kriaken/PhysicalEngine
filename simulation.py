from particle import *
from vector import *
from wall import *
import pygame

#Simulation class includes particles, walls(borders) and forces, that act on it particles. It also provides time evolution
class Simulation:

    def __init__(self, particles, walls, width, height, gravity, dt, substeps, k = 1):
        self.time = 0
        self.particles = particles
        self.width = width
        self.height = height
        self.dt = (dt/substeps)/1000
        self.substeps = substeps
        self.g = gravity
        self.k = k

        if len(walls) != 0:

            self.walls = walls

            self.find_wall("top").setPosition(0)
            self.find_wall("bottom").setPosition(self.height)
            self.find_wall("left").setPosition(0)
            self.find_wall("right").setPosition(self.width)
        else:
            self.walls = [Wall("top", 0, 0, 0), Wall("bottom", 0, 0, height), Wall("left", 0, 0, 0), Wall("right", 0, 0, width)]

    #Function to evolute system in time
    def time_step(self):
        i = 0

        #Colissions
        while(i < self.substeps):
            for j in range(len(self.particles)):
                #Walls collisions and scattering
                self.wall_collision(self.particles[j])
                for k in range(j+1, len(self.particles)):
                    if(circles_collision(self.particles[j], self.particles[k])):
                        #Scattering
                        circles_scatter(self.particles[j], self.particles[k], self.k)
            i+=1

        #Application of internal force (gravity)
        self.apply_gravity()

        #Changing kinematic parameters of particles using Euler`s numerical integration method
        for p in self.particles:
            p.move(self.dt*self.substeps)

        #Changing kinematic parameters of walls
        for wall in self.walls:
                wall.move(self.time, self.dt*self.substeps)
        
        self.time += self.dt*self.substeps

    #Function for drawing simulation box(field), where all particles are contained and all objects of the simulation
    def draw(self, screen):

        top_padding = bottom_padding = (0.1/0.9)*self.height/2
        left_padding = right_padding = (0.1/0.9)*self.width/2

        screen.fill("#333333")

        x = left_padding + self.find_wall("left").getPosition()
        y = top_padding + self.find_wall("top").getPosition()

        w = self.width - self.find_wall("left").getPosition() - (self.width - self.find_wall("right").getPosition())
        h = self.height - self.find_wall("top").getPosition() - (self.height - self.find_wall("bottom").getPosition())
        
        field = pygame.Rect(x, y, w, h)

        pygame.draw.rect(screen, "white", field)
        pygame.draw.rect(screen, "black", field, int(0.1*left_padding))

        for i in range(len(self.particles)):
            self.particles[i].draw(screen, self.particles[i].getPosition().X() + left_padding, self.particles[i].getPosition().Y() + top_padding)

    #Function for applying internal force(gravity)
    def apply_gravity(self):
        for j in range(len(self.particles)):
            self.particles[j].apply_force(self.particles[j].getMass()*self.g, self.dt*self.substeps)

    #Function for getting respective wall
    def find_wall(self, side):
        
        for wall in self.walls:
            if side == wall.getSide():
                return wall

        return 0

    #Function for collisions with walls
    def wall_collision(self, particle):

        if particle.getPosition().X() - self.find_wall("left").getPosition() < particle.getRadius():
            
            wall_scattering(particle, self.find_wall("left"), self.k)
        if particle.getPosition().X() > self.find_wall("right").getPosition() - particle.getRadius():

            wall_scattering(particle, self.find_wall("right"), self.k)
        if particle.getPosition().Y() - self.find_wall("top").getPosition() < particle.getRadius():
            
            wall_scattering(particle, self.find_wall("top"), self.k)
        if particle.getPosition().Y() > self.find_wall("bottom").getPosition() - particle.getRadius():
            
            wall_scattering(particle, self.find_wall("bottom"), self.k)

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height
        