import math
import numpy as np
from PIL import Image as im

width = 10
height = 10
target_width = 8
target_height = 8

def pic_calc(): #generates a greyscale image with the set width and height
    global pixels 
    pixels = np.zeros([width,height], dtype=np.uint8)

    for x in range(width):
        for y in range(height):
            pixels[x][y] = 255 - ((x+y)*(255/((width-1)+(height-1))))

def shape_calc(): #generates a list containing the relative values of the pixels by side
    global ratios
    width_ratio, height_ratio = width/target_width, height/target_height
    ratios = (width_ratio, height_ratio)

    shapes = [[], []]
    shape_lengths = [0, 0]

    for i in range(2): #generates corners
        corner_shape = []
        temp_rest = ratios[i]

        temp_shape_length = 0
        for _ in range(math.floor(temp_rest)):
            corner_shape.append(1)
            temp_shape_length += 1
            temp_rest -= 1

        corner_shape.append(temp_rest)
        temp_shape_length += 1

        if temp_shape_length > shape_lengths[i]: 
            shape_lengths[i] = temp_shape_length

        shapes[i].append(corner_shape)

        for _ in range(1, target_width): #i changed this here, idk if thats a problem, it was target_width-1 before. Pending investigation.
            temp_shape = []
            temp_shape_length = 0

            if temp_rest:
                temp_shape.append(1-temp_rest)
                temp_shape_length += 1

            temp_rest += ratios[i]
            temp_rest -= 1

            for _ in range(math.floor(temp_rest)):
                temp_shape.append(1)
                temp_shape_length += 1
                temp_rest -= 1

            temp_shape.append(temp_rest)
            temp_shape_length += 1

            if temp_shape_length > shape_lengths[i]:
                shape_lengths[i] = temp_shape_length

            shapes[i].append(temp_shape)

        shapes[i].append(corner_shape[::-1])

    return shapes[0], shapes[1], shape_lengths[0], shape_lengths[1]

def shrink_calc():
    global pixel_split

    pixel_split = np.zeros([target_width, target_height, width_shape_length, height_shape_length])

    for x in range(target_width):
        for y in range(target_height):
            for i in range(len(width_shape[x])):
                for j in range(len(height_shape[y])):
                    pixel_split[x][y][i][j] = width_shape[x][i]*height_shape[y][j]

def map():
    global pixel_split, target_image

    target_image = np.zeros([target_width,target_height], dtype=np.uint8)

    temp_val = 0
    temp_div = ratios[0]*ratios[1]
    modifier = [0, 0]

    for x in range(target_width):
        for y in range(target_height):
            for i in range(len(width_shape[x])):
                for j in range(len(height_shape[y])):
                    temp_val += pixels[x+modifier[0]][y+modifier[1]]*pixel_split[x][y][i][j]

            target_image[x][y] = temp_val/temp_div
            temp_val = 0

pic_calc()
width_shape, height_shape, width_shape_length, height_shape_length = shape_calc()
shrink_calc()
map()

target_out = target_image.astype(np.int8)

target = im.fromarray(target_out)
target.save("test_product.png")

out = pixels.astype(np.uint8)

image = im.fromarray(pixels)
image.save("test.png")