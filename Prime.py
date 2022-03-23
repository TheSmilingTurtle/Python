import math 
import time

plist = [2]

try:
    num = int(input(">>>"))
except:
    print("Thats not an int")

def check(x):
    square_root = int(math.sqrt(x))
    for i in plist:
        if i > square_root:
            break
        elif not x%i:
            return False
    return True

def run(t):    
    for i in range(3, t, 2):
        if check(i):
            plist.append(i)

def printer():
    print(plist)
    print("There are", len(plist), "prime numbers")
    print("It took", elapsed/(10**6), "ms")

start = time.time_ns()
run(num)
elapsed = time.time_ns()-start

printer()