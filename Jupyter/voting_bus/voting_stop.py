import matplotlib.pyplot as plt
import math
import numpy as np
import random
from pprint import pprint, pformat
from functools import reduce

ITER_NUM = 10000

PEOPLE = 100
STOPS = 20

ROUTE_LENGTH = 10
ROUTE_COUNT = 20

wait_times = []

stop_dir = {x: 0 for x in range(STOPS)}

class Route:
    def __init__(self, stops={}):
        if stops:
            self.stops = stops
        else:
            self.stops = {random.randint(0, STOPS-1) for i in range(ROUTE_LENGTH)}
        
    def count_votes(self):
        return sum(stop_dir[stop] for stop in self.stops)
    
    def reset_votes(self):
        for stop in self.stops:
            stop_dir[stop] = 0
    
    def __repr__(self):
        return pformat(self.stops)

class Agency:
    def __init__(self, n, non_intersecting=False): #currently, non_intersecting does nothing
        self.routes = [Route() for _ in range(n-1)]

    def fill_blanks(self):
        self.routes += [Route(stop_dir.keys() - set().union(*[route.stops for route in self.routes]) )]
    
    def __repr__(self):
        return pformat({i: r for i, r in enumerate(self.routes)})

class Person:
    def __init__(self):
        self.stop = random.randint(0, STOPS-1)
        self.wait = 0
    
    def vote(self):
        stop_dir[self.stop] += 1
        self.wait += 1
    
class Population:
    def __init__(self):
        self.people = {Person() for _ in range(PEOPLE)}

    def vote(self):
        for person in self.people:
            person.vote()
    
    def add_people(self, n):
        self.people = self.people.union({Person() for _ in range(n)})
    
    def filter(self, f):
        original_length = len(self.people)
        staying = {person for person in self.people if not f(person)}
        rejects = self.people - staying
        self.people = staying

        wait_times.append(max(rejects, key=lambda x: x.wait).wait)

        return original_length - len(self.people)
    
    def __repr__(self):
        return pformat({i: p.stop for i, p in enumerate(self.people)})

population = Population()

agency = Agency(ROUTE_COUNT)
agency.fill_blanks()

records = np.zeros(ITER_NUM)
#wait_times = []

for i in range(ITER_NUM):
    population.vote()

    #select stop
    chosen = agency.routes[np.argmax([route.count_votes() for route in agency.routes])]

    #record data
    records[i] = chosen.count_votes()

    #reset_votes of the routes stops
    chosen.reset_votes()

    #change out people
    n = population.filter(lambda x: x.stop in chosen.stops)
    population.add_people(n)

wait_times = np.array(wait_times)

print("Mean wait: ", wait_times.mean())
print("Max wait: ", wait_times.max())

print("Proper wait: ", wait_times.mean()*( ROUTE_LENGTH / ROUTE_COUNT ))

plt.scatter(np.arange(len(wait_times)), wait_times)
plt.show()