import numpy as np
from PIL import Image

field = np.random.randint(0,2,(1000, 1000))

def displace(a, v, top_left, bottom_right):
    top, left = top_left
    bottom, right = bottom_right
    x, y = v

    left -= x
    
    a[left:right, top:bottom] = 

im = Image.fromarray(255*field.astype(np.uint8))
im.save("out/out0.png")
