import math
import time
import matplotlib.pyplot as plt

iterations = 10000000

max_number = 0
max_number_iterations = 0
numbers_list = []
counters_list = []
print_list = []

def banana(n):
    num = n
    counter = 0

    while num != 1:
        match num%2:
            case 1:
                num = 3*num +1
            case 0:
                num = num/2

        counter += 1
    
    return counter

t0 = time.time()

for i in range(1, iterations):
    calculation_num = banana(i)
    
    if calculation_num > max_number_iterations:
        max_number = i
        max_number_iterations = calculation_num
        numbers_list.append(i)
        counters_list.append(calculation_num)
        print_list.append((i, calculation_num))

t_elapsed = time.time() - t0

print(max_number, max_number_iterations)
print(t_elapsed)

print(print_list)

d_jump = 0
jump_list = []

for i in range(1, len(print_list)):
    jump = print_list[i][1]-print_list[i-1][1]

    if jump > d_jump:
        d_jump = jump
        jump_list.append((d_jump, (print_list[i-1][0], print_list[i][0])))
    
print(jump_list)

plt.scatter(numbers_list, counters_list, s = 2)
plt.show()