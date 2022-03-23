import numpy as np
import matplotlib.pyplot as plt

maxit = int(input("Degree of precision = "))
h = int(input("Image sidelength = "))
w = h

def mandelbrot(h,w, maxit=maxit):
    y,x= np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z**2+c
        diverge= z*np.conj(z)> 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now]=i
        z[diverge]=2
        #print((i/maxit)*100,"%")
    return divtime

plt.imshow(mandelbrot(h,w))
plt.show()