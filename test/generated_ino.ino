#include <PlotterV3.h>
#define a 1

Plt plot = Plt();

void setup()
{
    servo.attach(4);
	delay(500);
	up();
    plot.draw_line(70*a, 12*a);
    down();
	delay(500);
	plot.draw_line(-7*a, 0*a);
	delay(500);
	plot.draw_line(3*a, -12*a);
	delay(500);
	plot.draw_line(-59*a, 0*a);
	delay(500);
	plot.draw_line(-6*a, 31*a);
	delay(500);
	plot.draw_line(23*a, 0*a);
	delay(500);
	plot.draw_line(2*a, -8*a);
	delay(500);
	plot.draw_line(-14*a, 0*a);
	delay(500);
	plot.draw_line(1*a, -4*a);
	delay(500);
	plot.draw_line(14*a, 0*a);
	delay(500);
	plot.draw_line(1*a, -7*a);
	delay(500);
	plot.draw_line(-14*a, 0*a);
	delay(500);
	plot.draw_line(1*a, -4*a);
	delay(500);
	plot.draw_line(22*a, 0*a);
	delay(500);
	plot.draw_line(-5*a, 23*a);
	delay(500);
	plot.draw_line(10*a, 0*a);
	delay(500);
	plot.draw_line(4*a, -23*a);
	delay(500);
	plot.draw_line(8*a, 0*a);
	delay(500);
	plot.draw_line(-4*a, 23*a);
	delay(500);
	plot.draw_line(9*a, 0*a);
	delay(500);
	plot.draw_line(3*a, -12*a);
	delay(500);
	plot.draw_line(7*a, 0*a);
	delay(500);
	plot.draw_line(-3*a, 12*a);
	delay(500);
	plot.draw_line(10*a, 0*a);
	delay(500);
	plot.draw_line(6*a, -31*a);
	delay(500);
	plot.draw_line(-9*a, 0*a);
	delay(500);
	up();
	delay(500);
	up();
    plot.draw_line(-32*a, -8*a);
    down();
	delay(500);
	plot.draw_line(3*a, 0*a);
	delay(500);
	plot.draw_line(1*a, -4*a);
	delay(500);
	plot.draw_line(-3*a, 0*a);
	delay(500);
	up();
	delay(500);
	up();
    plot.draw_line(-34*a, 12*a);
    down();
	delay(500);
	plot.draw_line(3*a, 0*a);
	delay(500);
	plot.draw_line(1*a, -4*a);
	delay(500);
	plot.draw_line(-3*a, 0*a);
	delay(500);
	up();
	delay(500);
	up();
    plot.draw_line(21*a, 4*a);
    down();
	delay(500);
	plot.draw_line(3*a, 0*a);
	delay(500);
	plot.draw_line(1*a, -4*a);
	delay(500);
	plot.draw_line(-3*a, 0*a);
	delay(500);
	up();
	delay(500);
	up();
    plot.draw_line(-15*a, 10*a);
    down();
	delay(500);
	plot.bezier_c(10*a, 6*a, 6*a, 10*a, 5*a, 17*a);
	delay(500);
	delay(500);
	plot.bezier_c(5*a, 25*a, 8*a, 28*a, 12*a, 28*a);
	delay(500);

    up();
}

void loop()
{
    //have you heard of the colour green?
}