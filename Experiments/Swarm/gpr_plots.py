import threading
import time
import numpy as np

from mystic.solvers import diffev2
from mystic.monitors import VerboseMonitor

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

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
        self.bounds = [BOUNDS[0], BOUNDS[1]]*self.steps + [(-MAX_SPEED, MAX_SPEED)]*(2*self.steps-2)

        self.goal_gpr = GaussianProcessRegressor(kernel=RBF(length_scale=1, length_scale_bounds="fixed") + WhiteKernel())
        self.danger_gpr = GaussianProcessRegressor(kernel=RBF(length_scale=1, length_scale_bounds="fixed") + WhiteKernel())

        self.goal_X = np.array([[]])
        self.goal_y = np.array([[]])
  
        self.danger_X = np.array([[]])
        self.danger_y = np.array([[]])

    def refit(self):
        self.goal_gpr.fit(self.goal_X, self.goal_y)
        self.danger_gpr.fit(self.danger_X, self.danger_y)

    def move(self):
        self.pos += self.velocity*dt
    
    def plan(self):
        self.refit()

        #stepmon = VerboseMonitor(1)

        solution = diffev2(self.opt_function,self.initial_guess, maxiter=20,bounds=self.bounds, disp=True, constraints=self.model_constraint, tightrange=True)

        self.velocity = np.array([solution[2*self.steps], solution[2*self.steps+1]])

        #print(list(zip(solution, self.bounds)))

        self.initial_guess[0:2*self.steps-2] = solution[2:2*self.steps] # MPC style shifting
        self.initial_guess[2*self.steps:-2] = solution[2*self.steps+2:]

        self.initial_guess[2*self.steps-2:2*self.steps] = solution[2*self.steps-2:2*self.steps] #duplicate last velocity and positio
        self.initial_guess[-2:] = solution[-2:]
    
    def opt_function(self, x):
        objective = 0 - 0.01*sum(x[i]**2 + x[i+1]**2 for i in range(2*self.steps,4*self.steps-2, 2))
        objective += sum(-np.log(1-self.danger_gpr.predict([(x[i], x[i+1])])[0]) for i in range(0,2*self.steps-2, 2))
        objective -= 2*sum((ret := self.goal_gpr.predict([(x[i], x[i+1])], return_std=True))[0] + ret[1] for i in range(0,2*self.steps-2, 2))
        #this is awful pls rewrite

        return objective
    
    def velocity_constraint(self, x): # unused
        return sum(x[i]**2 + x[i+1]**2 - MAX_SPEED for i in range(2*self.steps,4*self.steps-2, 2))

    def model_constraint(self, x):
        x[0] = self.pos[0]
        x[1] = self.pos[1]

        for i in range(0,2*self.steps-2,2):
            x[i+2] = x[i] + dt*x[2*self.steps+i]
            x[i+3] = x[i+1] + dt*x[2*self.steps+i+1]

        return x

    def communicate(self, drones, measurements):
        pos = self.pos.reshape(1,-1) + dt*self.velocity.reshape(1,-1)

        print(measurements)
        print(pos)
        print()

        if self.danger_X.size == 0:
            self.danger_X = pos
            self.danger_y = np.array([[measurements["danger"]]])
            self.goal_X = pos
            self.goal_y = np.array([[measurements["goal"]]])
        else:
            self.danger_X = np.vstack((self.danger_X, pos))
            self.danger_y = np.vstack((self.danger_y, [[measurements["danger"]]]))
            self.goal_X = np.vstack((self.goal_X, pos))
            self.goal_y = np.vstack((self.goal_y, [[measurements["goal"]]]))

        for drone in drones:
            if drone.danger_X.size == 0:
                drone.danger_X = pos
                drone.danger_y = np.array([[measurements["danger"]]])
                drone.goal_X = pos
                drone.goal_y = np.array([[measurements["goal"]]])
            else:
                drone.danger_X = np.vstack((drone.danger_X, pos))
                drone.danger_y = np.vstack((drone.danger_y, [[measurements["danger"]]]))
                drone.goal_X = np.vstack((drone.goal_X, pos))
                drone.goal_y = np.vstack((drone.goal_y, [[measurements["goal"]]]))

    def dist(self, drone):
        return np.linalg.norm(self.pos - drone.pos)
    
class Tree:
    def __init__(self, pos, width, noise):
        self.pos = pos
        self.width = width
        self.noise = noise
    
    def sdf(self, drone): # this might be causing instability
        return np.max(np.linalg.norm(drone.pos + dt*drone.velocity - self.pos) - self.width - drone.width, 0) # also maybe use  - self.width - drone.width

    def noisy_sdf(self, drone):
        return self.sdf(drone) #+ np.random.normal(0,self.noise)

class Goal:
    def __init__(self, pos, width, noise):
        self.pos = pos
        self.width = width
        self.noise = noise
    
    def sdf(self, drone): # this might be causing instability
        return np.max(np.linalg.norm(self.pos - drone.pos - dt*drone.velocity), 0) # also maybe use  - self.width - drone.width

    def noisy_sdf(self, drone):
        return self.sdf(drone) #+ np.random.normal(0,self.noise)


BOUNDS = ([0, 10], [0, 10])
MAX_SPEED = 1

dt=1

Goals = [Goal(np.array([5,9]), 0.2, 0)]
Trees = [Tree(np.array([6,6]), 0.3, 0), Tree(np.array([2, 3]), 0.3, 0), Tree(np.array([1,3]), 0.3, 0), Tree(np.array([3,4]), 0.3, 0)]
Drones = [Drone(np.array([1,1]), 0.1), Drone(np.array([2,2]), 0.1), Drone(np.array([3,3]), 0.1)]

NEAREST_N = 3

def loop():
    while True:
        simulate()

def simulate():
    for drone in Drones:
        tmp = Drones.copy()
        tmp.remove(drone)

        tmp = sorted(tmp, key=lambda x: drone.dist(x))

        measurements = {"danger": sum(np.exp(-tree.noisy_sdf(drone)) for tree in Trees)/len(Trees), "goal": sum(np.exp(-goal.noisy_sdf(drone)) for goal in Goals)} #compute the danger samples here

        drone.communicate(tmp, measurements)            
    
    for drone in Drones:
        drone.plan()
        drone.move()

x = np.linspace(*BOUNDS[0], 100)
y = np.linspace(*BOUNDS[1], 100)
x, y = np.meshgrid(x, y)
points = np.column_stack((x.ravel(), y.ravel()))

def plot():
    global fig, axs

    simulate()

    # for i, drone in enumerate(Drones):
    #     z_danger = drone.danger_gpr.predict(points).reshape(x.shape)
    #     z_goal = drone.goal_gpr.predict(points, return_std=True)

    #     axs[i].clear()

    #     axs[i].contourf(x, y, z_danger - z_goal[0].reshape(x.shape) - z_goal[1].reshape(x.shape), alpha=0.5, cmap='Reds')
    #     #axs[i].contourf(x, y, z_danger, alpha=0.5, cmap='Reds')
    #     #axs[i].contourf(x, y, z_goal[0].reshape(x.shape), alpha=0.5, cmap='Greens')
    #     axs[i].set_title(f'Drone {i+1}')

    z_danger = Drones[0].danger_gpr.predict(points).reshape(x.shape)
    z_goal = Drones[0].goal_gpr.predict(points, return_std=True)

    axs[0].clear()
    axs[1].clear()
    axs[2].clear()

    axs[0].contourf(x, y, -np.log(1-z_danger) - 2*z_goal[0].reshape(x.shape) - 2*z_goal[1].reshape(x.shape), alpha=0.5, cmap='Blues')
    axs[1].contourf(x, y, z_danger, alpha=0.5, cmap='Reds')
    axs[2].contourf(x, y, z_goal[0].reshape(x.shape), alpha=0.5, cmap='Greens')

    axs[1].scatter(Drones[0].danger_X[:,0], Drones[0].danger_X[:,1], c=Drones[0].danger_y, alpha=1, cmap='Reds')
    axs[2].scatter(Drones[0].goal_X[:,0], Drones[0].goal_X[:,1], c=Drones[0].goal_y, alpha=1, cmap='Greens')

    axs[0].set_xlim(*BOUNDS[0])
    axs[0].set_ylim(*BOUNDS[1])
    axs[1].set_xlim(*BOUNDS[0])
    axs[1].set_ylim(*BOUNDS[1])
    axs[2].set_xlim(*BOUNDS[0])
    axs[2].set_ylim(*BOUNDS[1])

    axs[-1].clear()
    axs[-1].set_xlim(*BOUNDS[0])
    axs[-1].set_ylim(*BOUNDS[1])

    for tree in Trees:
        axs[-1].add_patch(Circle(tuple(tree.pos), tree.width, color='red'))

    for goal in Goals:
        axs[-1].add_patch(Circle(tuple(goal.pos), goal.width, color='green'))

    for i, drone in enumerate(Drones):
        axs[-1].add_patch(Circle(tuple(drone.pos), drone.width, color='blue'))
        axs[-1].arrow(drone.pos[0]-drone.velocity[0]*dt, drone.pos[1]-drone.velocity[1]*dt, drone.velocity[0]*dt, drone.velocity[1]*dt, head_width=0.1, head_length=0.1, color='orange')

    plt.draw()
    plt.pause(0.01)

sim = threading.Thread(target=loop)
sim.daemon = True


fig, axs = plt.subplots(1, 4, figsize=(40, 10))
#                          len(Drones) +1
#sim.start()

while True:
    plot()