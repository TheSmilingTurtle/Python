import numpy as np
from numba import njit, prange
import matplotlib.pyplot as plt
from rich import print
import time
import datetime

@njit(parallel=True)
def calc():
    top    = 1j
    left   = -2
    bottom = -1j
    right  = 0.5

    Nr = 2500
    Ni = 2000
    N = 200

    r = np.linspace(left, right, Nr).astype(np.complex128)
    i = np.linspace(top, bottom, Ni).reshape(-1,1)

    r, i = np.broadcast_arrays(r, i)

    c = r+i #np.mgrid[top:bottom:Ni*1j, left:right:Nr*1j].sum(axis=0)

    z = np.zeros_like(c)

    for _ in range(N):
        z = z**2 + c

    z = np.where(np.abs(z) <= 4, z, 0)

    return z

start = time.time()
z = calc()
end = time.time()
print(f"First time: {datetime.timedelta(seconds=end-start)}")

start = time.time()
z = calc()
end = time.time()
print(f"Second time: {datetime.timedelta(seconds=end-start)}")

plt.imshow(np.abs(z))
plt.show()

