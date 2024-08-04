import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, b):
        return Vector(self.X() + b.X(), self.Y() + b.Y())
    
    def __mul__(self, c):
        return Vector(c*self.X(), c*self.Y())
    
    def __rmul__(self, c):
        return self.__mul__(c)
    
    def __sub__(self, b):
        return Vector(self.X() - b.X(), self.Y() - b.Y())

    def X(self):
        return self.x

    def Y(self):
        return self.y
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    
    def vector_length(self):
        return (self.X()**2 + self.Y()**2)**(1/2)

def dot_product(a, b):
    return Vector(a.X()*b.X(), a.Y()*b.Y())

def angle_vectors(a, b):
    return math.acos(dot_product(a, b)/(a.vector_length()*b.vector_length()))

def cross_product(a, b):
    phi = angle_vectors(a, b)

    return a.vector_length()*b.vector_length()*math.sin(phi)