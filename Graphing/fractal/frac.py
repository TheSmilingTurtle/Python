from PIL import Image
from tqdm import tqdm
import math
import cmath

TOTAL = (4,2)
SIZE = (2000,1000)

OFFSET = (2,-1)

SIZE_X = SIZE[0]
SIZE_Y = SIZE[1]

img = Image.new("RGB", SIZE, "black")
pixel = img.load()

def func(z: complex, c: complex):
    return c*z*(1-z)

def colour(i: int) -> "tuple[int, int, int]":
    #return (i*7+20,i**2+20,int(i**3*1/15)+50)
    return (i*5+100,i*5,i*5+100) 

def getcomplex(x: int, y: int) -> complex:
    return (x/SIZE_X * TOTAL[0] ) - OFFSET[0] + ((-y/SIZE_Y * TOTAL[1]) - OFFSET[1]) * 1j

for x in tqdm(range(SIZE_X)):
    for y in range(SIZE_Y):
        z = 0.2
        c = getcomplex(x,y)
        for i in range(50):
            z = func(z,c)
            if abs(z)>100:
                pixel[x,y] = colour(i)
                break
        else:
            pixel[x,y] = (0,0,0)

for x in tqdm(range(SIZE_X)):
    for y in range(SIZE_Y):
        z = 0.2
        c = getcomplex(x,y)
        for i in range(50):
            z = func(z,c)
            if abs(z)>100:
                pixel[x,y] = colour(i)
                break
        else:
            pixel[x,y] = (0,0,0)

img.save("/home/thesmilingturtle/coding/Python//Graphing/fractal/test.png")
