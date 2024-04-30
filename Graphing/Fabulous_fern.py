import matplotlib.pyplot as plt
import random
import modules.vector as vec

class dot:
    def __init__(self, position):
        self.pos = position
        self.trace_list = []
    
    def transform(self, vector1, vector2, coef1, coef2):
        self.pos.x = self.pos.dot(vector1) + coef1
        self.pos.y = self.pos.dot(vector2) + coef2
    
    def trace(self):
        self.trace_list.append(self.pos.copy())
    
    def draw_traces(self):
        out_list = [i.to_tuple() for i in self.trace_list]

        plt.scatter(*zip(*out_list), s = 0.1)

iterations = 1000000

point = dot(vec.vector2D(0, 0))

vec1 = vec.vector2D(0,0)
vec2 = vec.vector2D(0, 0.16)
vec3 = vec.vector2D(0.85, 0.04)
vec4 = vec.vector2D(-0.04, 0.85)
vec5 = vec.vector2D(0.2, -0.28)
vec6 = vec.vector2D(0.23, 0.22)
vec7 = vec.vector2D(-0.15, 0.28)
vec8 = vec.vector2D(0.26, 0.24)

for _ in range(iterations):
    point.trace()

    r = random.random()

    if r < 0.02:
        point.transform(vec1, vec2, 0, 0)
    elif r < 0.87:
        point.transform(vec3, vec4, 0, 1.6)
    elif r < 0.94:
        point.transform(vec5, vec6, 0, 1.6)
    else:
        point.transform(vec7, vec8, 0, 0.44)

point.draw_traces()

plt.show()