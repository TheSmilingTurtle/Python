class Particle:
    def __init__(self, x = 0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, _):
        return (self.x,self.y)
    
p = Particle()

print(p+0)