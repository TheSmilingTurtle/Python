#from rich import print
from rich.progress import track
from rich.traceback import install
install(show_locals=True)

from numba import njit, prange

print(16000000//73000//2-1)