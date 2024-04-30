import numpy as np 
from PIL import Image as im 

Nx, Ny = 1200, 800
ymin, ymax = -1, 1
xmin, xmax = -2, 1

x = np.linspace(xmin, xmax, Nx)
y = np.linspace(ymin, ymax, Ny)
xv, yv = np.meshgrid(x, y)

c = xv + 1j*yv
z =  np.zeros_like(c)

bd = np.zeros_like(c, dtype=np.uint8)

for _ in range(255):
    z = z**2 + c
    bd += np.abs(z) < 2

pic = im.fromarray(bd)
pic.save("brot.png")