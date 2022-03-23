import math
import matplotlib.pyplot as plt
iterations = 1000

lamb = 3.5
first_term = 0.2

x_list = [i for i in range(iterations)]
out_list = [first_term]

for i in x_list:
    out_list.append(lamb*out_list[i]*(1-out_list[i]))

x_list.append(iterations)

plt.scatter(x_list, out_list, s = 1)
plt.show()