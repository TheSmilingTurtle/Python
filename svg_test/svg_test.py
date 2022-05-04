from svg.path import parse_path
from svg.path.path import *
from xml.dom import minidom
from pprint import pprint

pa = input("Input path: ")
SCALING = float(input("Input scaling: "))

init = """#include <PlotterV3.h>
#include <Servo.h>

Plt plot = Plt();
Servo servo;

int agl = 170;

void down()
{
    for (; agl <= 170; ++agl)
    {
    servo.write(agl);
    delay(15);
   }
}

void up()
{
    for (; agl >= 120; --agl)
    {
    servo.write(agl);
    delay(15);
    }
}

void setup()
{
    servo.attach(4);
"""

conc = """}

void loop() {}"""

x = 0
y = 0

move_template = """
    up();
    plot.drawline(%d, %d);
    down();
"""

line_template = "\tplot.draw_line(%d, %d);\n"

cubic_bezier_template = "\tplot.bezier_c(%d, %d, %d, %d, %d, %d);\n"

quadratic_bezier_template = "\tplot.bezier_c(%d, %d, %d, %d);\n"

# read the SVG file
doc = minidom.parse(pa)

path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')] #try getting it by the path tag

if not path_strings:
    path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('svg:path')] #try getting it by the svg:path tag

doc.unlink()

with open("svg_test/generated_ino.ino", "w") as ino:
    ino.write(init) #initialise the file
    
    for path_string in path_strings:
        p = parse_path(path_string) #parser go brrrr

        for e in p:
            if isinstance(e, Move):
                #move to a given position
                ino.write(move_template % ( round((e.end.real-x)*SCALING), round((e.end.imag-y)*SCALING) ))

            elif isinstance(e, Line):
                #from absolute to relative, ende minus anfang
                ino.write(line_template % ( round((e.end.real-e.start.real)*SCALING), round((e.end.imag-e.start.imag)*SCALING )) )

            elif isinstance(e, CubicBezier):
                #cubic bezier
                ino.write(cubic_bezier_template % ( round(e.control1.real*SCALING), round(e.control1.imag*SCALING), round(e.control2.real*SCALING), round(e.control2.imag*SCALING), round(e.end.real*SCALING), round(e.end.imag*SCALING)) )

            elif isinstance(e, QuadraticBezier):
                #quadratic bezier
                ino.write(quadratic_bezier_template % (round(e.control.real*SCALING ), round(e.control.imag*SCALING), round(e.end.real*SCALING), round(e.end.imag*SCALING)))

            elif isinstance(e, Close):
                #Closing the shape
                ino.write(line_template % ( round((e.end.real-e.start.real)*SCALING), round((e.end.imag-e.start.imag)*SCALING )))

                ino.write("\tup();\n")

                break
            else: 
                #linearly approximate everything you do not know
                ino.write(line_template % ( round((e.end.real-x)*SCALING), round((e.end.imag-x)*SCALING )))

                pprint("Unknown instance:")
                pprint(e)
            
            #update coords
            x = e.end.real*SCALING
            y = e.end.imag*SCALING
    
    ino.write(conc) #finalise the file

print("\ndone") #heureca