from vector import *

class Particle:

    def __init__(self, position, velocity, mass, radius):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius

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
    
    def getRadius(self):
        return self.radius

    def setPosition(self, position):
        self.position = position

    def setVelocity(self, velocity):
        self.velocity = velocity


def collision(p1, p2):

    l = Vector(p1.getPosition().X() - p2.getPosition().X(), p1.getPosition().Y() - p2.getPosition().Y())

    if (l.vector_length()<=(p1.getRadius()+p2.getRadius())):
        return True

    return False

def scatter()