import random
import string
import contextlib
import tokenize
from keyword import kwlist

N = 1000
T = 10000

def generate_random_token():
    return 

class Evo:
    def __init__(self, code, loss_fn):
        self.code = code
        self.loss_fn = loss_fn
    
    def produce_offspring(self, n):
        offspring = []
        for _ in range(n):
            offspring.append(self.mutated_copy())
        return offspring
    
    def mutated_copy(self): #for now just append a random integer [0,3] of random bytes
        return Evo(self.code + ''.join(random.choices(string.printable, k=random.randint(0,3))), self.loss_fn)
    
    def loss(self, t=False): #compute
        ldict={}
        try:
            with contextlib.redirect_stderr(None):
                exec(self.code, {}, ldict) #so uhm, unsafe affffff but thats of right?
        except:
            return 200
        try:
            return self.loss_fn(ldict['x'])
        except:
            return 100

def loss_fn(x):
    return (abs(x-12.5))**2/1e4

population = [Evo('x=', loss_fn).mutated_copy() for _ in range(N)]

for _ in range(T):
    score_pairs = sorted([(x.loss(), x) for x in population], key=lambda x: x[0])[:N//2]
    population = [x[1] for x in score_pairs] + [Evo('x=', loss_fn).mutated_copy() for _ in range(N//4)]
    for i in range(N):
        population += population[i].produce_offspring(1+N//(2**(i+3)))
        if len(population) == N:
            break

    if _%100 == 0:
        print(score_pairs[0])
        print(population[0].code)
        print()
