from vector import *

#Class for supermassive walls with velocity as a function of time
class Wall:
    
    def __init__(self, side, acceleration_function = 0, velocity0 = 0, position = 0):
        self.side = side
        self.position = position
        self.acceleration_function = acceleration_function
        self.velocity = velocity0

    def setPosition(self, position):
        self.position = position

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity
    
    def getSide(self):
        return self.side