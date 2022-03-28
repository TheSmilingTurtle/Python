import numpy as np
from PIL import Image, ImageOps
from os import walk, remove

def mask(image, t):
    image[image < t] = 0
    image[image >= t] = 255

    return image

def find_black(image, max_height):
    for i in range(max_height):
        if 0 in image[i]:
            return i

def find_path(folder):
    filenames = next(walk(folder), (None, None, []))[2]

    return r"\\".join([folder, filenames[0]])

threshhold = 80
image_height_mm = 100
folder_path = "Pics"

filenames = next(walk(folder_path), (None, None, []))[2]

path = find_path(folder_path)

with Image.open(path) as pic:
    im = np.array(ImageOps.grayscale(pic))
    size = pic.size

del pic

im = mask(im, threshhold)
height_px = find_black(im, size[1])

del im
#remove(path)

height_mm = image_height_mm*(1-(height_px/size[1]))

print("The height is {0:.2f} mm".format(height_mm))