import pygame
import math
from vector import *
from wall import *

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

def wall_scattering(p, wall):
    i = Vector(1, 0)
    j = Vector(0, 1)

    if wall.getSide() == "top":
        p.setPosition(Vector(p.getPosition().X(), wall.getPosition() + p.getRadius()))
        p.setVelocity(Vector(p.getVelocity().X(), wall.getVelocity()) + (dot_product(j, p.getVelocity().Y())/math.abs(dot_product(j, p.getVelocity().Y())))*p.getVelocity().Y())
    elif wall.getSide() == "bottom":
        p.setPosition(Vector(p.getPosition().X(), wall.getPosition() - p.getRadius()))
        p.setVelocity(Vector(p.getVelocity().X(), wall.getVelocity()) + (dot_product(-j, p.getVelocity().Y())/math.abs(dot_product(-j, p.getVelocity().Y())))*p.getVelocity().Y())
    elif wall.getSide() == "left":
        p.setPosition(Vector(wall.getPosition() + p.getRadius(), p.getPosition().Y()))
        p.setVelocity(Vector(wall.getVelocity()) + (dot_product(i, p.getVelocity().X())/math.abs(dot_product(i, p.getVelocity().X())))*p.getVelocity().X(), p.getVelocity().Y())
    elif wall.getSide() == "right":
        p.setPosition(Vector(wall.getPosition() - p.getRadius(), p.getPosition().Y()))
        p.setVelocity(Vector(wall.getVelocity()) + (dot_product(-i, p.getVelocity().X())/math.abs(dot_product(-i, p.getVelocity().X())))*p.getVelocity().X(), p.getVelocity().Y())


def circles_scatter(p1, p2):

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

    v1f_x = ((2*m2)/(m1 + m2))*v21i_x
    v2f_x = ((m2 - m1)/(m1 + m2))*v21i_x

    p1.setVelocity(v1f_x + v1i)
    p2.setVelocity(v2f_x + v21i_y + v1i)

    dl = (p1.getRadius() + p2.getRadius()) - (p1.getPosition() - p2.getPosition()).vector_length()
    dr = p1.getPosition() - p2.getPosition()
    a = (p1.getPosition().Y() - p2.getPosition().Y())/(p1.getPosition().X() - p2.getPosition().X())

    dl1 = Vector((p1.getMass()/(p1.getMass() + p2.getMass()))*dl/math.sqrt(a**2 + 1), (a*(p1.getMass()/(p1.getMass() + p2.getMass()))*dl)/math.sqrt(a**2 + 1))
    dl2 = Vector((p2.getMass()/(p1.getMass() + p2.getMass()))*dl/math.sqrt(a**2 + 1), (a*(p2.getMass()/(p1.getMass() + p2.getMass()))*dl)/math.sqrt(a**2 + 1))

    if (dot_product(dr, dl1) < 0):
        dl1 = (-1)*dl1
    else:
        dl2 = (-1)*dl2

    p1.setPosition(p1.getPosition() + dl1)
    p2.setPosition(p2.getPosition() + dl2)

p1 = Particle(Vector(1, 0), Vector(1, 0), 1, 2)
p2 = Particle(Vector(2, 0), Vector(0, 0), 1, 2)

print(p1.getVelocity().X(), p1.getVelocity().Y(), p2.getVelocity().X(), p2.getVelocity().Y())

circles_scatter(p1, p2)

print("x1", p1.getPosition().X(), "y1", p1.getPosition().Y(), "x2", p2.getPosition().X(), "y2", p2.getPosition().Y())
print(p1.getVelocity().X(), p1.getVelocity().Y(), p2.getVelocity().X(), p2.getVelocity().Y())
