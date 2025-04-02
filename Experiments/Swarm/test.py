import threading
import time
import numpy as np

from scipy.optimize import Bounds, NonlinearConstraint

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.patches import Circle

class Drone:
    def __init__(self, pos, width):
        self.pos = pos.astype(np.float64)
        self.width = width
        self.velocity = np.array([0,0.01])

        self.goal_gpr = GaussianProcessRegressor(kernel=RBF())
        self.danger_gpr = GaussianProcessRegressor(kernel=RBF())

        self.goal_X = np.array([])
        self.goal_y = np.array([])
  
        self.danger_X = np.array([])
        self.danger_y = np.array([])

    def refit(self):
        self.goal_gpr.fit(self.goal_X, self.goal_y)
        self.danger_gpr.fit(self.danger_X, self.danger_y)

    def move(self, dt):
        self.pos += self.velocity*dt
    
    def plan(self):
        # use constraints similar to mpc and optimize  

        pass

    def communicate(self, drones):
        #send data to other drones
        pass
    
    def dist(self, drone):
        return np.linalg.norm(self.pos - drone.pos)
    
class Tree:
    def __init__(self, pos, width, noise):
        self.pos = pos
        self.width = width
        self.noise = noise
    
    def sdf(self, drones):
        return [np.linalg.norm(drone.pos - self.pos) - self.width - drone.width for drone in drones]

    def noisy_sdf(self, drones):
        return [dist + np.random.normal(0,self.noise) for dist in self.sdf(drones)]

BOUNDS = Bounds([-10, 10], [-10, 10])
MAX_SPEED = 1

SPEED_CONSTRAINT = NonlinearConstraint()


Trees = []
Drones = [Drone(np.array([1,1]), 0.1), Drone(np.array([2,2]), 0.1), Drone(np.array([3,3]), 0.1)]

NEAREST_N = 3

def simulate():
    while True:
        for drone in Drones:
            tmp = Drones.copy()
            tmp.remove(drone)

            tmp = sorted(tmp, key=lambda x: drone.dist(x))

            drone.communicate(tmp)

            drone.plan()
            drone.move(dt=0.1)
        time.sleep(0.1)
        

def plot(frame):
    for i, drone in enumerate(Drones):
        drone_circles[i].set(center=tuple(drone.pos))
    
    return drone_circles

sim = threading.Thread(target=simulate)
sim.daemon = True

fig, ax = plt.subplots(1,1)

ax.set_xlim(0,10)
ax.set_ylim(0,10)

drone_circles = [Circle(tuple(drone.pos), drone.width) for drone in Drones]

tree_circles = [Circle(tree.pos, tree.width) for tree in Trees]

for tree in tree_circles:
    fig.add_artist(tree)

for drone in drone_circles:
    fig.add_artist(drone)

a = ani.FuncAnimation(fig, plot)

input("Enter to start sim")

sim.start()

plt.show()
