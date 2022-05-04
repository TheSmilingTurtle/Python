from svg.path import parse_path
from svg.path.path import *
from xml.dom import minidom
from pprint import pprint

SCALING = 5

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
doc = minidom.parse('svg_test/ETH_Zurich_Logo_black_1.svg')
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
if not path_strings:
    path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('svg:path')]

doc.unlink()

with open("svg_test/generated_ino.ino", "w") as ino:
    ino.write(init)
    
    for path_string in path_strings:
        p = parse_path(path_string)
        #pprint(p)
        for e in p:
            pprint(e)
            if isinstance(e, Move):
                ino.write(move_template % ( (e.end.real-x)*SCALING, (e.end.imag-y)*SCALING ))
                x = e.end.real*SCALING
                y = e.end.imag*SCALING
            elif isinstance(e, Line):
                ino.write(line_template % ( (e.end.real-e.start.real)*SCALING, (e.end.imag-e.start.imag)*SCALING ))
                x = e.end.real*SCALING
                y = e.end.imag*SCALING
            elif isinstance(e, CubicBezier):
                ino.write(cubic_bezier_template % ( e.control1.real*SCALING, e.control1.imag*SCALING, e.control2.real*SCALING, e.control2.imag*SCALING, e.end.real*SCALING, e.end.imag*SCALING))
                x = e.end.real*SCALING
                y = e.end.imag*SCALING
            elif isinstance(e, QuadraticBezier):
                ino.write(quadratic_bezier_template % (e.control.real*SCALING, e.control.imag*SCALING, e.end.real*SCALING, e.end.imag*SCALING))
                x = e.end.real*SCALING
                y = e.end.imag*SCALING
            elif isinstance(e, Close):
                ino.write(line_template % ( (e.end.real-e.start.real)*SCALING, (e.end.imag-e.start.imag)*SCALING ))
                ino.write("\tup();\n")
                x = e.end.real*SCALING
                y = e.end.imag*SCALING

            else: 
                pprint("unknown instance:")
                pprint(e)
    
    ino.write(conc)

print("\ndone")