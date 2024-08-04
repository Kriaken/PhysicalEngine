import pygame
import math
from vector import *

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

class Particle(RigidBody):

    def __init__(self, position, velocity, mass, radius):
        super().__init__(position, velocity, mass)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, "black", (self.getPosition().X(), self.getPosition().Y()), self.getRadius())


def circles_collision(p1, p2):

    l = Vector(p1.getPosition().X() - p2.getPosition().X(), p1.getPosition().Y() - p2.getPosition().Y())

    if (l.vector_length()<=(p1.getRadius()+p2.getRadius())):
        return True

    return False

def circles_scatter(p1, p2):

    v1i = p1.getVelocity()
    v2i = p2.getVelocity()

    m1 = p1.getMass()
    m2 = p2.getMass()

    v1f = ((m1 - m2)/(m1 + m2))*v1i + ((2*m2)/(m1 + m2))*v2i
    v2f = ((m2 - m1)/(m1 + m2))*v2i + ((2*m1)/(m1 + m2))*v1i

    p1.setVelocity(v1f)
    p2.setVelocity(v2f)

    dl = (p1.getRadius() + p2.getRadius()) - (p1.getPosition() - p2.getPosition()).vector_length()
    dr = p1.getPosition() - p2.getPosition()
    a = (p1.getPosition().X() - p2.getPosition().X())/(p1.getPosition().Y() - p1.getPosition().Y())

    dl1 = Vector((p1.getMass()/(p1.getMass() + p2.getMass()))*dl/math.sqrt(a**2 + 1), (a*(p1.getMass()/(p1.getMass() + p2.getMass()))*dl)/math.sqrt(a**2 + 1))
    dl2 = Vector((p2.getMass()/(p1.getMass() + p2.getMass()))*dl/math.sqrt(a**2 + 1), (a*(p2.getMass()/(p1.getMass() + p2.getMass()))*dl)/math.sqrt(a**2 + 1))

    if (dot_product(dr, dl1) < 0):
        dl1 = (-1)*dl1
    else:
        dl2 = (-1)*dl2

    p1.setPosition(p1.getPosition() + dl1)
    p2.setPosition(p2.getPosition() + dl2)

p1 = Particle(Vector(1, 1), Vector(1, 1), 1, 2)
p2 = Particle(Vector(2, 1), Vector(1, 1), 1, 2)

v1 = Vector(1, 1)
v2 = Vector(1, 1)

print(2.5*v2.Y())

print(circles_scatter(p1, p2))
