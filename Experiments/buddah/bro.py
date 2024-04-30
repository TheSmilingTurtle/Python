import numpy as np 
from PIL import Image as im 
from tqdm import tqdm
import matplotlib.pyplot as plt

class Plane:
    def __init__(self, x_lim, y_lim, size):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.size = size

    def init_plane(self):
        x = np.linspace(xmin, xmax, Nx)
        y = np.linspace(ymin, ymax, Ny)
        xv, yv = np.meshgrid(x, y)

        self.data = xv + 1j*yv
        return self

    def init_zeros(self):
        self.data = np.zeros((Ny, Nx))
        return self
    
    def zeros_like(p):
        return Plane(
            p.x_lim,
            p.y_lim,
            p.size
        ).init_zeros()
    
    def plane_like(p):
        return Plane(
            p.x_lim,
            p.y_lim,
            p.size
        ).init_plane()

    def copy(p):
        k = Plane.zeros_like(p)
        k.data = p.data.copy()
        return k
    @property
    def xmin(self):
        return self.x_lim[0]
    
    @property
    def xmax(self):
        return self.x_lim[1]
    
    @property
    def ymin(self):
        return self.y_lim[0]
    
    @property
    def ymax(self):
        return self.y_lim[1]
    
    @property
    def Nx(self):
        return self.size[0]

    @property
    def Ny(self):
        return self.size[1]
    
    @property
    def width(self):
        return self.xmax - self.xmin
    
    @property
    def height(self):
        return self.ymax - self.ymin
    
    def lies_within(self, key):
        real = np.real(key)
        imag = np.imag(key)

        return np.logical_and( 
            np.logical_and(self.xmin <= real, real <= self.xmax), 
            np.logical_and(self.ymin <= imag, imag <= self.ymax)
            )
    
    def map_to_index(self, key):
        key_x = np.uint32( ( np.real(key) + 1e-6 - self.xmin) / ( self.width  ) * (self.Nx-1) )
        key_y = np.uint32( ( np.imag(key) + 1e-6 - self.ymin) / ( self.height ) * (self.Ny-1) )

        return key_y, key_x
    
    def __getitem__(self, key):
        key_y, key_x = self.map_to_index(key)

        return self.data[key_y, key_x]
    
    def __setitem__(self, key, val):
        key_y, key_x = self.map_to_index(key)

        self.data[key_y, key_x] = val

N = 255

Nx, Ny = 1200//2, 800//2
ymin, ymax = -1, 1
xmin, xmax = -2, 1


c = Plane(
    (xmin, xmax),
    (ymin, ymax),
    (Nx, Ny)
).init_plane()

bd = np.zeros_like(c.data, dtype=np.float32)

z = np.zeros((c.Ny, c.Nx, N+1), dtype=np.complex128)

for i in tqdm(range(N)):
    z[..., i+1] = z[..., i]**2 + c.data

z[np.isnan(z)] = np.inf
_z = z[np.abs(z[..., -1]) > 2]
_z = _z[c.lies_within(_z)]
np.add.at(bd, c.map_to_index(_z), 1)

bd[c.map_to_index(0+0j)] = 1

bd = 1-np.exp(-np.square(bd)/bd.max())*np.exp(1/bd.max())

pic = im.fromarray((bd * 255).astype(np.uint8))
pic.save("buddha.png")