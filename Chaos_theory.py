import math
import matplotlib.pyplot as plt
iterations = 100
precision = 100000
first_term = 0.2

min_lamb = -2
max_lamb = 4

x_list = []
y_list = []

max_lamb -= min_lamb

for i in range(precision):
    out_list = [first_term]
    lamb = min_lamb + (max_lamb*i)/precision

    for j in range(iterations):
        n = out_list[j]
        out_list.append(lamb*n*(1-n))
    
    new_list = len(set(out_list[-20:]))#list(set(out_list[-20:]))

    y_list.append(new_list)
    x_list.append(lamb)
    #for k in new_list:
    #    y_list.append(k)
    #    x_list.append(lamb)

plt.scatter(x_list, y_list, s = 0.1)
plt.show()