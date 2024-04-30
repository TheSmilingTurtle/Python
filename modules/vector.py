import math

class vector2D:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    
    def __str__(self):
        return "(({}, {}))".format(self.x, self.y)
    
    def __repr__(self):
        return "(({}, {}))".format(self.x, self.y)

    def __add__(self, other_vector):
        return vector2D(self.x + other_vector.x, self.y + other_vector.y)
    
    def __sub__(self, other_vector):
        return vector2D(self.x - other_vector.x, self.y - other_vector.y)
    
    def __mul__(self, factor):
        return vector2D(self.x * factor, self.y * factor)
    
    def __truediv__(self, factor):
        return vector2D(self.x / factor, self.y / factor)
    
    def __abs__(self):
        return (math.sqrt(self.x**2 + self.y**2))
    
    def copy(self):
        return vector2D(self.x, self.y)
    
    def to_tuple(self):
        return (self.x, self.y)
    
    def to_list(self):
        return [self.x, self.y]
    
    def dot(self, other_vector):
        return self.x * other_vector.x + self.y * other_vector.y
    
    def norm(self):
        return vector2D(-self.y, self.x)

    def rotate(self, angle):
        self.x = self.x*math.cos(angle) - self.y*math.sin(angle)
        self.y = self.x*math.sin(angle) + self.y*math.cos(angle)
    
    def rotated(self, angle):
        return vector2D(self.x*math.cos(angle) - self.y*math.sin(angle), self.x*math.sin(angle) + self.y*math.cos(angle))