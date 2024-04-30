import math
pi = math.pi
its = 10**7

def Wallis(n):
    if n == 1:
        return 4/3
    h = 4*n**2
    k = h-1

    return (h/k)*Wallis(n-1)

def approx(n):
    if not n:
        return 1

    u = 1 - 2*(n%2)                     #(-1)^i
    
    return (u/(2*n+1)) + approx(n-1)

approx = approx(998)*4
Wallis = Wallis(998)*2

print("Other  Recursive: ", approx, "  Error: ", (pi - approx)**2)
print("Wallis Recursive: ", Wallis, " Error: ", (pi - Wallis)**2)

pi1 = 0

for i in range(its):
    u = 1 - 2*(i%2)             #(-1)^i

    pi1 += (u/(2*i+1))

pi1 *= 4

print("Other  Linear:    ", pi1, " Error: ", (pi-pi1)**2)

pi2 = 2

for i in range(1, its):
    n = 4*(i**2)
    k = n-1

    pi2 *= n/k

print("Wallis Linear:    ", pi2, " Error: ", (pi - pi2)**2)

print("\nActual PI:        ", pi, "  Error:  Undefined")