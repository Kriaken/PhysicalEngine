import pygame
import math
from vector import *
from wall import *

#RigidBody is an arbitral physical object, that can interact with other objects. Used as ancestor for specific physical bodies
class RigidBody:

    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def move(self, dt):
        self.setPosition(Vector(self.getPosition().X() + self.getVelocity().X()*dt, self.getPosition().Y() + self.getVelocity().Y()*dt))

    def apply_force(self, F, dt):
        self.setVelocity(Vector(self.getVelocity().X() + (F.X()/self.getMass())*dt, self.getVelocity().Y() + (F.Y()/self.getMass())*dt))

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity
    
    def getMass(self):
        return self.mass

    def setPosition(self, position):
        self.position = position

    def setVelocity(self, velocity):
        self.velocity = velocity

#Descendant class of RigidBody class. Describes particle as round physical body
class Particle(RigidBody):

    def __init__(self, position, velocity, mass, radius):
        super().__init__(position, velocity, mass)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def draw(self, screen, x=0, y=0):
        if x and y:
            pygame.draw.circle(screen, (255 , 0, 0), (x, y), self.getRadius())
        else:
            pygame.draw.circle(screen, (255, 0, 0), (self.getPosition().X(), self.getPosition().Y()), self.getRadius())

#Function to detect collision beetwen objects of Particle class
def circles_collision(p1, p2):

    l = Vector(p1.getPosition().X() - p2.getPosition().X(), p1.getPosition().Y() - p2.getPosition().Y())

    if (l.vector_length()<=(p1.getRadius()+p2.getRadius())):
        return True

    return False

#Function for scattering Particles of supermassive walls of Simulation box
def wall_scattering(p, wall, k=1):

    if wall.getSide() == "top":
        p.setPosition(Vector(p.getPosition().X(), wall.getPosition() + p.getRadius()))
        p.setVelocity(Vector(p.getVelocity().X(), -k*p.getVelocity().Y() + (1 + k)*wall.getVelocity()))
    elif wall.getSide() == "bottom":
        p.setPosition(Vector(p.getPosition().X(), wall.getPosition() - p.getRadius()))
        p.setVelocity(Vector(p.getVelocity().X(), -k*p.getVelocity().Y() - (1 + k)*wall.getVelocity()))
    elif wall.getSide() == "left":
        p.setPosition(Vector(wall.getPosition() + p.getRadius(), p.getPosition().Y()))
        p.setVelocity(Vector(-k*p.getVelocity().X() + (1 + k)*wall.getVelocity(), p.getVelocity().Y()))
    elif wall.getSide() == "right":
        p.setPosition(Vector(wall.getPosition() - p.getRadius(), p.getPosition().Y()))
        p.setVelocity(Vector(-p.getVelocity().X() - 2*wall.getVelocity(), p.getVelocity().Y()))

#Function for scattering Particles
def circles_scatter(p1, p2, k=1):

    v1i = p1.getVelocity()
    v2i = p2.getVelocity()

    m1 = p1.getMass()
    m2 = p2.getMass()

    i_versor = (p1.getPosition() - p2.getPosition())
    i_versor.normalize()

    j_versor = Vector(-i_versor.Y(), i_versor.X())

    #v1i = v1i - v1i
    v21i = (v2i - v1i)

    v21i_x = v21i.project_onto(i_versor)
    v21i_y = v21i.project_onto(j_versor)

    v1f_x = (((1 + k)*m2)/(m1 + m2))*v21i_x
    v2f_x = ((m2 - k*m1)/(m1 + m2))*v21i_x

    p1.setVelocity(v1f_x + v1i)
    p2.setVelocity(v2f_x + v21i_y + v1i)

    dl = (p1.getRadius() + p2.getRadius()) - (p1.getPosition() - p2.getPosition()).vector_length()
    dr = p1.getPosition() - p2.getPosition()
    dr.normalize()

    dl1 = (p1.getMass()/(p1.getMass() + p2.getMass()))*dl*dr

    dl2 = -(p2.getMass()/(p1.getMass() + p2.getMass()))*dl*dr

    #a = (p1.getPosition().Y() - p2.getPosition().Y())/(p1.getPosition().X() - p2.getPosition().X())
#
    #dl1 = Vector((p1.getMass()/(p1.getMass() + p2.getMass()))*dl/math.sqrt(a**2 + 1), (a*(p1.getMass()/(p1.getMass() + p2.getMass()))*dl)/math.sqrt(a**2 + 1))
    #dl2 = Vector((p2.getMass()/(p1.getMass() + p2.getMass()))*dl/math.sqrt(a**2 + 1), (a*(p2.getMass()/(p1.getMass() + p2.getMass()))*dl)/math.sqrt(a**2 + 1))
#
    #if (dot_product(dr, dl1) < 0):
    #    dl1 = (-1)*dl1
    #else:
    #    dl2 = (-1)*dl2

    p1.setPosition(p1.getPosition() + dl1)
    p2.setPosition(p2.getPosition() + dl2)