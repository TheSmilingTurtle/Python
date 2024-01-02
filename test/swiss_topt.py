import numpy as np
import laspy
import matplotlib.pyplot as plt

las = laspy.read("2539_1166.las")

coords = np.vstack((las.x, las.y, las.z)).transpose()

print(coords.shape)

coords = coords[coords[:,0] < 2539105]
coords = coords[coords[:,1] < 1166180]
coords = coords[coords[:,0] > 2539100]
coords = coords[coords[:,1] > 1166145]

fig = plt.figure()
ax = plt.axes(projection='3d')

THINNING = 1

ax.scatter3D(coords[:,0][::THINNING], coords[:,1][::THINNING], coords[:,2][::THINNING], s=1, c=coords[:,2][::THINNING], cmap="inferno")

mi = coords[:,2].min()
ma = coords[:,2].max()
height = ma - mi

print(f"{mi=}\n{ma=}\n{height=}")
plt.show()