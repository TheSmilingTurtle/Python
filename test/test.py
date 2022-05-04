import random
from pprint import pprint

x = 0
y = 0

init = r"""#include <PlotterV3.h>
#define a 1

Plt plot = Plt();

void setup()
{
    servo.attach(4);
"""

sassy_comments = ["im chaotic", "have you heard of the colour green?", "ma mate Dave", "Oh, this ones great"]

with open("test\\nic_coords.txt", "r") as file:
    with open("test\\generated_ino.ino", "w") as ino:
        ino.write(init);
        for line in file:
            rand = random.random()

            info = [x.strip() for x in line.split(",")]

            start = info.pop(0).lower()

            values = [round(float(x)) for x in info if x != ""]

            ino.write("\tdelay(500);\n")

            if start == "l" or start == "h":
                ino.write("\tplot.draw_line({}*a, {}*a);\n".format(values[0]-x, values[1]-y))

                x = values[0]
                y = values[1]

            elif start == "c":
                values.pop(0)
                values.pop(0)

                ino.write("\tplot.bezier_c({});\n".format(", ".join([str(x)+"*a" for x in values])))

                x = values[4]
                y = values[5]
            
            elif start == "m":
                ino.write("""\tup();
    plot.draw_line({}*a, {}*a);
    down();
""".format(values[0]-x, values[1]-y))

                x = values[0]
                y = values[1]
            
            elif start == "z":
                ino.write("\tup();\n")
            
        ino.write("""
    up();
}

void loop()
{"""+"""
    //{}""".format(random.choice(sassy_comments))+"""
}""" \
                );