import threading
import time
import numpy as np

from mystic.solvers import fmin_powell
from mystic.monitors import VerboseMonitor

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

from rich import print

import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.patches import Circle, Arrow

class Drone:
    def __init__(self, pos, width):
        self.pos = pos.astype(np.float64)
        self.width = width
        self.velocity = np.array([0,0])

        self.steps = 6

        self.initial_guess = list(self.pos)*self.steps + list(1-2*np.random.random(2*self.steps - 2))
        self.bounds = [(-10, 10), (-10, 10)]*self.steps + [(-1, 1)]*(2*self.steps-2)

        self.goal_gpr = GaussianProcessRegressor(kernel=RBF())
        self.danger_gpr = GaussianProcessRegressor(kernel=RBF())

        self.goal_X = np.array([[]])
        self.goal_y = np.array([[]])
  
        self.danger_X = np.array([[]])
        self.danger_y = np.array([[]])

    def refit(self):
        self.goal_gpr.fit(self.goal_X, self.goal_y)
        self.danger_gpr.fit(self.danger_X, self.danger_y)

    def move(self):
        self.pos += self.velocity
    
    def plan(self):
        self.refit()

        stepmon = VerboseMonitor(1)

        solution = fmin_powell(self.opt_function,self.initial_guess, bounds=self.bounds, disp=True, constraints=self.model_constraint, itermon=stepmon)

        self.velocity = np.array([solution[2*self.steps], solution[2*self.steps+1]])

        self.initial_guess[0:2*self.steps-2] = solution[2:2*self.steps] # MPC style shifting
        self.initial_guess[2*self.steps:-2] = solution[2*self.steps+2:]

        self.initial_guess[2*self.steps-2:2*self.steps] = solution[2*self.steps-2:2*self.steps] #duplicate last velocity and positio
        self.initial_guess[-2:] = solution[-2:]
    
    def opt_function(self, x):
        objective = 0
        objective += sum(self.danger_gpr.predict([(x[i], x[i+1])])[0] for i in range(0,2*self.steps-2, 2))
        objective -= sum((ret := self.goal_gpr.predict([(x[i], x[i+1])], return_std=True))[0] + ret[1] for i in range(0,2*self.steps-2, 2))
        #this is awful pls rewrite

        return objective
    
    def velocity_constraint(self, x):
        sum(x[i]**2 + x[2*self.steps]**2 - 1 for i in range(self.steps-1))

    def model_constraint(self, x):
        x[0] = self.pos[0]
        x[1] = self.pos[1]

        for i in range(0,2*self.steps-2, 2):
            x[i+2] = x[i] + x[2*self.steps+i]
            x[i+3] = x[i+1] + x[2*self.steps+i+1]

        return x

    def communicate(self, drones, measurements):
        if self.danger_X.size == 0:
            self.danger_X = self.pos
            self.danger_y = np.array([[measurements["danger"]]])
            self.goal_X = self.pos
            self.goal_y = np.array([[measurements["goal"]]])
        else:
            self.danger_X = np.vstack((self.danger_X, self.pos))
            self.danger_y = np.vstack((self.danger_y, [[measurements["danger"]]]))
            self.goal_X = np.vstack((self.goal_X, self.pos))
            self.goal_y = np.vstack((self.goal_y, [[measurements["goal"]]]))

        for drone in drones:
            if drone.danger_X.size == 0:
                drone.danger_X = self.pos
                drone.danger_y = np.array([[measurements["danger"]]])
                drone.goal_X = self.pos
                drone.goal_y = np.array([[measurements["goal"]]])
            else:
                drone.danger_X = np.vstack((drone.danger_X, self.pos))
                drone.danger_y = np.vstack((drone.danger_y, [[measurements["danger"]]]))
                drone.goal_X = np.vstack((drone.goal_X, self.pos))
                drone.goal_y = np.vstack((drone.goal_y, [[measurements["goal"]]]))


    def dist(self, drone):
        return np.linalg.norm(self.pos - drone.pos)
    
class Tree:
    def __init__(self, pos, width, noise):
        self.pos = pos
        self.width = width
        self.noise = noise
    
    def sdf(self, drone):
        return np.linalg.norm(drone.pos - self.pos) - self.width - drone.width

    def noisy_sdf(self, drone):
        return self.sdf(drone) + np.random.normal(0,self.noise)

class Goal:
    def __init__(self, pos, width, noise):
        self.pos = pos
        self.width = width
        self.noise = noise
    
    def sdf(self, drone):
        return np.linalg.norm(drone.pos - self.pos) - self.width - drone.width

    def noisy_sdf(self, drone):
        return self.sdf(drone) + np.random.normal(0,self.noise)


BOUNDS = ((-10, 10), (-10, 10))
MAX_SPEED = 1

dt=1

Goals = [Goal(np.array([5,9]), 0.2, 1)]
Trees = [Tree(np.array([6,6]), 0.3, 0.1), Tree(np.array([2, 3]), 0.3, 0.1), Tree(np.array([1,3]), 0.3, 0.1), Tree(np.array([3,4]), 0.3, 0.1)]
Drones = [Drone(np.array([1,1]), 0.1), Drone(np.array([2,2]), 0.1), Drone(np.array([3,3]), 0.1)]

NEAREST_N = 3

def simulate():
    while True:
        for drone in Drones:
            tmp = Drones.copy()
            tmp.remove(drone)

            tmp = sorted(tmp, key=lambda x: drone.dist(x))

            measurements = {"danger": sum(tree.noisy_sdf(drone) for tree in Trees), "goal": sum(goal.noisy_sdf(drone) for goal in Goals)} #compute the danger samples here

            drone.communicate(tmp, measurements)            
        
        for drone in Drones:
            drone.plan()
            drone.move()

        time.sleep(0.1)
        
contours = []
drone_circles = []
drone_arrows = []

for i, drone in enumerate(Drones):
    ax = plt.subplot(1, len(Drones)+1, i+1)
    ax.set_xlim(*BOUNDS[0])
    ax.set_ylim(*BOUNDS[1])
    
    x = np.linspace(*BOUNDS[0], 100)
    y = np.linspace(*BOUNDS[1], 100)
    x, y = np.meshgrid(x, y)
    points = np.column_stack((x.flatten(), y.flatten()))
    z_danger = drone.danger_gpr.predict(points).reshape(x.shape)
    z_goal = drone.goal_gpr.predict(points).reshape(x.shape)

    contour_danger = ax.contourf(x, y, z_danger, alpha=0.5)
    contour_goal = ax.contourf(x, y, z_goal, alpha=0.5)
    contours.append(contour_danger)
    contours.append(contour_goal)

    circle = Circle(tuple(drone.pos), drone.width, edgecolor='black', facecolor='blue', alpha=0.5)
    ax.add_patch(circle)
    drone_circles.append(circle)

    arrow = Arrow(drone.pos[0], drone.pos[1], drone.velocity[0], drone.velocity[1], width=0.1, edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(arrow)
    drone_arrows.append(arrow)

fig, axs = plt.subplots(1, len(Drones)+1, figsize=(20, 5))

for ax in axs:
    ax.set_xlim(*BOUNDS[0])
    ax.set_ylim(*BOUNDS[1])

with ax as axs[-1]:
    for tree in Trees:
        circle = Circle(tuple(tree.pos), tree.width, edgecolor='black', facecolor='green', alpha=0.5)
        ax.add_patch(circle)

    for goal in Goals:
        circle = Circle(tuple(goal.pos), goal.width, edgecolor='black', facecolor='red', alpha=0.5)
        ax.add_patch(circle)

def plot(frame):
    global contours, drone_circles, drone_arrows

    for i, drone in enumerate(Drones):
        ax = axs[i]
        
        x = np.linspace(*BOUNDS[0], 100)
        y = np.linspace(*BOUNDS[1], 100)
        x, y = np.meshgrid(x, y)
        points = np.column_stack((x.flatten(), y.flatten()))
        z_danger = drone.danger_gpr.predict(points).reshape(x.shape)
        z_goal = drone.goal_gpr.predict(points).reshape(x.shape)

        # ax.cla()
        # ax.set_xlim(*BOUNDS[0])
        # ax.set_ylim(*BOUNDS[1])
        
        contour_danger = ax.contourf(x, y, z_danger, alpha=0.5)
        contour_goal = ax.contourf(x, y, z_goal, alpha=0.5)
        contours[2*i] = contour_danger
        contours[2*i+1] = contour_goal

        drone_circles[i].center = tuple(drone.pos)

        arrow = Arrow(drone.pos[0], drone.pos[1], drone.velocity[0], drone.velocity[1], width=0.1, edgecolor='black', facecolor='red', alpha=0.5)
        drone_arrows[i] = arrow

    ax = plt.subplot(1, len(Drones)+1, len(Drones)+1)
    
    ax.set_xlim(*BOUNDS[0])
    ax.set_ylim(*BOUNDS[1])

    for tree in Trees:
        circle = Circle(tuple(tree.pos), tree.width, edgecolor='black', facecolor='green', alpha=0.5)
        ax.add_patch(circle)

    for goal in Goals:
        circle = Circle(tuple(goal.pos), goal.width, edgecolor='black', facecolor='red', alpha=0.5)
        ax.add_patch(circle)

    for drone in Drones:
        circle = Circle(tuple(drone.pos), drone.width, edgecolor='black', facecolor='blue', alpha=0.5)
        ax.add_patch(circle)

    return contours + drone_circles + drone_arrows


sim = threading.Thread(target=simulate)
sim.daemon = True

input("Enter to start sim")

sim.start()

ani.FuncAnimation(plt.gcf(), plot, interval=100, blit=True)

plt.show()
