import matplotlib.pyplot as plt
import random
import math
import vector as vec

class dot:
    def __init__(self, x, y):
        self.position = vec.vector2D(x, y)
        self.trace_list = []

    def move(self, vector):
        self.position += vector

    def trace(self):
        self.trace_list.append(self.position)

    def draw_path(self):
        out_list = [i.to_tuple() for i in self.trace_list]

        plt.scatter(*zip(*out_list), s=0.1)

class circle_shape:
    def __init__(self, num, radius, centre):
        self.edge_num = num
        self.radius = radius
        self.edge_positions = []
        self.centre = centre

    def calculate_shape(self):
        pointer = vec.vector2D(0, self.radius)

        angle = math.pi*(2/self.edge_num)
        self.edge_positions = [
            self.centre + pointer.rotated(i*angle) for i in range(self.edge_num)]

    def draw_self(self):
        out_list = [i.to_tuple() for i in self.edge_positions]

        plt.scatter(*zip(*out_list), s=20)

try:
    number = int(input("Enter the number of points: "))
except:
    number = 3

try:
    iterations = int(input("Enter the number of iterations: "))
except:
    iterations = 10000

# Definitions
radius = 50
buffer = 10
coef = (number-2)/(number-1)
centre = vec.vector2D(buffer + radius, buffer + radius)

# create shape
shape = circle_shape(number, radius, centre)
shape.calculate_shape()

# create trace point
point = dot(random.randint(0, 100), random.randint(0, 100))

for _ in range(iterations):
    point.trace()
    point.move((random.choice(shape.edge_positions) - point.position) * coef)

# figure definitions
plt.figure(figsize=(7, 7))
plt.xlim(0, (radius + buffer)*2)
plt.ylim(0, (radius + buffer)*2)

# draw the recorded paths
point.draw_path()
shape.draw_self()

plt.show()
