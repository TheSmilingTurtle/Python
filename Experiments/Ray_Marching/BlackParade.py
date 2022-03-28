import math
from PIL import Image as img
import numpy as np

sphere_radii = np.array([10, 10])
spheres = np.array([ [[10], [5], [5]],
                     [[10], [8], [-8]] ])

number_of_objects = len(spheres)

pic_length, pic_height = 100, 100
pic_length_distance, pic_height_distance = 25, 25
pic = np.zeros((pic_length, pic_height), dtype=np.float64)
pixel_size = 0.25

camera_position = np.array([[-10], [0], [0]], dtype=np.float64)
image_plane = np.array([[0], [0], [0]])
image_plane_size = np.array([pic_length_distance, pic_height_distance])
top_left = np.array([[image_plane[0, 0]], [-pic_length_distance/2], [pic_height_distance/2]])

abs_dist = np.array([np.linalg.norm(i - camera_position) for i in spheres])

max_steps = 30
min_dist = 0.001
max_dist = int(np.max(abs_dist + sphere_radii)) + 1

def dist_calc(pos):
    normalised = np.array([np.linalg.norm(i - pos) for i in spheres])
    dist = normalised - sphere_radii
    
    return np.min(dist)

def walk(e_vector, pos):
    dist = dist_calc(pos)
    vec = e_vector*dist
    pos += vec

    return pos, dist

def march(e_vector):
    global camera_position
    steps = 0
    total_dist = 0
    pos = camera_position.copy()
    hit = False

    for i in range(max_steps):
        steps = i
        pos, step_dist = walk(e_vector, pos)
        total_dist += step_dist

        if step_dist <= min_dist:
            hit = True
            break
        elif total_dist >= max_dist:
            break
    
    return hit, total_dist, steps

def colour(args):
    value = args[0]
    if value:
        value = 1/math.sqrt(args[1])
    else:
        value = 0.27

    return value

def image_grid(z_pos, y_pos):
    pixel_pos = top_left + pixel_size*np.array([[0], [y_pos], [-z_pos]])
    vec = pixel_pos - camera_position
    
    return vec/np.linalg.norm(vec)

def render():
    global pic
    for i in range(pic_height):
        for j in range(pic_length):
            pic[i, j] = colour(march(image_grid(i, j)))
    
    pic = pic - np.min(pic)

    maximum = np.max(pic)

    pic = ((pic/maximum)*255)

render()

out = pic.astype(np.uint8)

picture = img.fromarray(out, "L")
picture.save("Ray_marching_test.png")