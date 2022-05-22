import math
import time

try:
    num = int(input("Enter a number: "))
except:
    print("Thats not an int")

temp_list = [x for x in range(2, num+1)]
primes_list = []

def frog(j,c):                      #bc it jumps
    global temp_list
    dist = int(num/j)               #decides how many times a jump needs to be executed

    for i in range(1, dist):        #executes the jumps
        temp_list[j*i+c] = None     #sets values at jump to None for easy filtering
                                        # it is in the form distance * jump index + starting point

def run():
    global primes_list
    limiter = int(math.sqrt(num))       #only necessary to check below the square root of num
    counter = 0

    while counter < limiter:
        jump = temp_list[counter]
        if not jump:                #skip if empty
            counter += 1
            continue

        frog(jump, counter)

        counter += 1
        
    primes_list = [x for x in temp_list if x]   #filtering
    return primes_list

def printer():
    if num <= 100:
        print(primes_list)
    print("\nThere are {} prime numbers".format(len(primes_list)))
    print("The last prime is".format(num), primes_list[-1])
    print("This took {}ms".format(duration))

t0 = time.time()
primes_list = run()
duration = (time.time()-t0)*1000

printer()