import matplotlib.pyplot as plt
import numpy as np

#series definitions
iterations = 80

#desired element definitions
end_values = 20
starting_element_index = iterations-end_values

#graph definitions
precision = 3000
round_num = 2

#positioning rectangle
top_left = -2.1 + 1.2j#-1.6 + 0.3j #
bottom_right = 4.1 - 1.2j#-0.9 - 0.3j #

def series(x, lamb):
    '''Calculated the series a[n] = r*a[n-1]*(1-a[n-1])'''

    return lamb*x*(1-x)

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

def chaos(index, lamb):
    '''Calculates the remaining series calculations,
    stores them in a list and returns counter() of the list'''

    series_list = np.zeros((*lamb.shape, end_values+1), dtype=np.complex128)
    series_list[..., 0] = element(index, lamb)

    for k in range(end_values):
            x = series_list[..., k]                  #previous element of the series
            series_list[..., k+1] = series(x, lamb)

    series_list = np.std(series_list, axis=2)
    series_list[~(series_list <= 1)] = -1
    
    return series_list
    
    series_list = np.abs(series_list).mean(axis=2)
    series_list[~(series_list <= 1)] = 0
    series_list[series_list == 0] = -1
    return series_list

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
vertical_precision = int(precision*quotient)+1

vertical_step_length = (max_imag_lamb - min_imag_lamb)/vertical_precision
horizontal_step_length = (max_real_lamb - min_real_lamb)/precision

#image array definitions
out_array = np.zeros([vertical_precision, precision], dtype=np.uint8)

lamb_re = np.linspace(min_real_lamb, max_real_lamb, precision).reshape(1,-1)
lamb_im = np.linspace(max_imag_lamb, min_imag_lamb, vertical_precision).reshape(-1,1)

lamb = lamb_re + 1j*lamb_im

im_array = chaos(starting_element_index, round_num, lamb)

plt.imshow(im_array, extent=(min_real_lamb, max_real_lamb, min_imag_lamb, max_imag_lamb))
plt.show()
