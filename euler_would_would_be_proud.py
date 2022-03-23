import numpy as np

iterations = 100

def factorial(n):
    if n == 1:
        return 1
    return np.longdouble(n * factorial(n-1))

def euler(its):
    if its == 0:
        return 1
    return np.longdouble(1/factorial(its)+euler(its-1))

print("{:.200}".format(np.longdouble(euler(iterations))))