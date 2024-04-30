from PIL import Image
import numpy as np

# i had a hunch this wouldn't work

N_STRIPES = 4

im = Image.open("in.png")

arr = np.array(im)

HALF = arr.shape[1]//2

STRIPE_WIDTH = HALF//N_STRIPES

arr1 = arr[:, 0:HALF]
arr2 = arr[:, HALF:]

a = np.hstack(list(sum([(arr1[:, i*STRIPE_WIDTH:(i+1)*STRIPE_WIDTH], arr2[:, i*STRIPE_WIDTH:(i+1)*STRIPE_WIDTH]) for i in range(N_STRIPES)], ())))

#magic stripe generator, creates a list of tuples containing the stripes, then flatten them with list(sum( l, () ))

i = Image.fromarray(a)
i.save("out.png")

im1 = Image.fromarray(arr1)
im2 = Image.fromarray(arr2)

im2.save("2.png")
im1.save("1.png")
im2.save("2.png")
