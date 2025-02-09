import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

#series definitions
iterations = 80

#desired element definitions
end_values = 20
starting_element_index = iterations-end_values

#graph definitions
precision = 1000
round_num = 2

#positioning rectangle
top_left_corner = -2.1 + 1.2j
bottom_right_corner = 4.1 - 1.2j

def complex_round(x, rounding):
    '''Round complex numbers'''

    return complex(round(x.real, rounding), round(x.imag, rounding))

def series(n, lamb):
    '''Calculated the series a[n] = r*a[n-1]*(1-a[n-1])'''

    return lamb*n*(1-n)

def element(n, lamb):
    '''Recursive definition to quicly calculate the first desired element.
    Everything below this element is not desired.
    '''
    first_term = 0.2

    if n == 0:
        return first_term
    else:
        #hacky, but works
        prev_element = element(n-1, lamb)

        return lamb*prev_element*(1-prev_element)

def counter(l):
    '''Counts number of identical elements in a list'''

    used = set()
    count = 0

    for i in l:                     #iterates over the list
        if i not in used:
            count += 1
            used.add(i)             #stores already seen values in a set

    return count

def chaos(index, round, lamb):
    '''Calculates the remaining series calculations,
    stores them in a list and returns counter() of the list'''

    series_list = [element(index, lamb)]

    for k in range(end_values):
            n = series_list[k]                  #previous element of the series
            series_list.append(series(n, lamb))

    return counter([complex_round(i, round) for i in series_list])

def fractal(horizontal_precision, top_left, bottom_right, round_val):

    #calculating the positioning
    min_imag_lamb = bottom_right.imag
    max_imag_lamb = top_left.imag

    min_real_lamb = top_left.real
    max_real_lamb = bottom_right.real

    #calculating rectangle lengths
    total_vertical_dist = max_imag_lamb - min_imag_lamb
    total_horizontal_dist = max_real_lamb - min_real_lamb

    #quotient for scaling
    quotient = total_vertical_dist/total_horizontal_dist

    #scaling
    vertical_precision = int(horizontal_precision*quotient)+1

    vertical_step_length = (max_imag_lamb - min_imag_lamb)/vertical_precision
    horizontal_step_length = (max_real_lamb - min_real_lamb)/horizontal_precision

    #image array definitions
    out_array = np.zeros([vertical_precision, horizontal_precision], dtype=np.uint8)

    for i in tqdm(range(vertical_precision)):
        #imaginary component of lambda for each row of the matrix
        lamb_imaginary = max_imag_lamb - vertical_step_length*i

        for j in range(horizontal_precision):
            #lambda complex
            lamb = complex(min_real_lamb + horizontal_step_length*j, lamb_imaginary)

            #feed the image
            out_array[i, j] = chaos(starting_element_index, round_val, lamb)

    return out_array

im_array = fractal(precision, top_left_corner, bottom_right_corner, round_num)

plt.imshow(im_array)
plt.show()
