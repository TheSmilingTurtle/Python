import matplotlib.pyplot as plt
import bezier

ax = plt.subplot()
curve = bezier.bezier("", [(0,0)])
curve.get_types()

with open("test\\nic_coords.txt") as file:
    for line in file:
        uncleaned = line.strip().split(" ")
        if uncleaned[-1] == ",":
            uncleaned.pop()
        cleaned = [float(x.replace(",", "").strip()) for x in uncleaned[1:]]
        paired = [(x, y) for x, y in zip(cleaned, cleaned[1::2])]
        temp = bezier.bezier(uncleaned[0].strip(), paired)
        temp.get_types()
        curve.add(temp)

print(curve.types)

curve.build_path()

ax.add_patch(curve.get_path)

plt.xlim(-300, 600)
plt.ylim(-300, 600)

plt.show()