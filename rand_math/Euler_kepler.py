import math
import numpy as np
import matplotlib.pyplot as plt

planet_position = np.array([4.946e11, 0], dtype = np.float64)
planet_velocity = np.array([0, 7941.9], dtype = np.float64)

star_position = np.array([0, 0])
star_gravity_parameter_for_roy = 1.32712442099e20 #Gravity parameter of the star

star_gravity = -star_gravity_parameter_for_roy

acceleration = np.array([0, 0])

dt = 86400
tmax = 1e8
n = int(tmax/dt)+1

x_positions = []
y_positions = []

x_positions.append(planet_position[0])
y_positions.append(planet_position[1])

for i in range(n):
    radius = np.linalg.norm(planet_position)

    try:
        acceleration = star_gravity*planet_position/math.pow(radius, 3)
    except:
        break

    planet_velocity += acceleration*dt
    planet_position += planet_velocity*dt

    x_positions.append(planet_position[0])
    y_positions.append(planet_position[1])

plt.scatter(x_positions, y_positions)
plt.scatter(star_position[0], star_position[1])
plt.show()