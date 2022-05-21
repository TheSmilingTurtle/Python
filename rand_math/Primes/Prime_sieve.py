from math import sqrt, ceil
import time

NUMBER = int(input("Enter a number: "))

dirty_list = [x for x in range(2, NUMBER+1)]

LIM = ceil(sqrt(NUMBER))

start = time.time()

for i in range(0, LIM):
    jump = dirty_list[i]

    if jump:
        for j in range(1, int(NUMBER/jump)):
            dirty_list[i+j*jump] = None;

clean_list = [x for x in dirty_list if x]

duration = time.time() - start;

if NUMBER <= 100:
    print(clean_list)

print()
print("There are {} primes.".format(len(clean_list)))
print("It took {}ms".format(duration*1000))