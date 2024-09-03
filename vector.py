import math

#Custom Vector class describing 2D vector with methods and functions for vector algebra
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
    
    def normalize(self):
        length = self.vector_length()
        
        self.setX(self.X()/length)
        self.setY(self.Y()/length)
        
    #Function to get projection of given vector a on vector b
    def project_onto(self, b):
        if (b.vector_length() != 1):
            return (dot_product(self, b)*b)*math.pow(b.vector_length(), -2)
        return dot_product(self, b)*b

#Function for dot product of two vectors
def dot_product(a, b):
    return a.X()*b.X() + a.Y()*b.Y()

#Function for calculating the angle between two vectors
def angle_vectors(a, b):
    return math.acos(dot_product(a, b)/(a.vector_length()*b.vector_length()))

#Function for cross product of two vectors
def cross_product(a, b):
    phi = angle_vectors(a, b)

    return a.vector_length()*b.vector_length()*math.sin(phi)