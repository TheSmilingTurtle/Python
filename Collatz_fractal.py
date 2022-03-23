import matplotlib.pyplot as plt
import math
import numpy as np

max_iterations = 100

#graph definitions
precision = 2000

# -1.05 + 0.05j
# -0.95 - 0.05j
#   --> cool

top_left_corner = -4.1 + 0.8j
bottom_right_corner = 4.1 - 0.8j

def complex_cos(n):
    real_part = n.real
    imaginary_part = n.imag

    return math.cos(real_part)*math.cosh(imaginary_part) - math.sin(real_part)*math.sinh(imaginary_part)*1j

def banana(n):
    num = n
    num_list = []
    counter = 0

    while counter < max_iterations:
        counter += 1

        num = (1/4)*(2 + 7*num - (2 + 5*num)*complex_cos(num*math.pi))

        if abs(num) > 226:
            return counter
        if num in num_list:
            return counter
        else:
            num_list.append(num)

    return counter

def fractal(horizontal_precision, top_left, bottom_right):
    
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

    for i in range(vertical_precision):
        #imaginary component of lambda for each row of the matrix
        lamb_imaginary = max_imag_lamb - vertical_step_length*i

        for j in range(horizontal_precision):
            #lambda complex
            lamb = complex(min_real_lamb + horizontal_step_length*j, lamb_imaginary)

            #feed the image
            out_array[i, j] = banana(lamb)
    
    return out_array

im_array = fractal(precision, top_left_corner, bottom_right_corner)

plt.imshow(im_array)
plt.show()