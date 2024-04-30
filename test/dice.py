import numpy as np
import time

start = time.time()

def dice_conv(dice, num, target):
    arr = np.ones(dice)/dice

    r = arr.copy()

    for n in range(num-1):
        r = np.convolve(r, arr)

    return r[target-num]

def dice_conv_pruned(dice, num, target):
    if target < num:
        return None
    elif target > num*dice:
        return None
    
    arr = np.ones(dice)/dice

    r = arr.copy()

    for _ in range(N1):
        r = np.convolve(r, arr)
    
    mean = dice * (num + 1) / num
    if target < mean:
        for _ in range(N2):
            r = np.convolve(r, arr)[dice-1:]
    elif target > mean:
        for _ in range(N3):
            r = np.convolve(r, arr)[:-dice+1]
    
    for _ in range(N4):
            r = np.convolve(r, arr)[dice-1:-dice+1]

    return r[0]


result = dice_conv(6, 100, 350)

elapsed = time.time() - start

print(f"{result = }, {elapsed = }s")