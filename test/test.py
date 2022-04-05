import matplotlib.pyplot as plt
import bezier

curve = bezier.bezier("c", [(0, 0), (0, 1), (1, 1)])

print(curve.points)

curve.build_path()

ax = plt.subplot()

ax.add_patch(curve.get_path)

plt.show()