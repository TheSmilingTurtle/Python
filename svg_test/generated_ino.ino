#include <PlotterV3.h>
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

    up();
    plot.drawline(70, 12);
    down();
	plot.draw_line(-6, 0);
	plot.draw_line(2, -12);
	plot.draw_line(-58, 0);
	plot.draw_line(-6, 31);
	plot.draw_line(23, 0);
	plot.draw_line(1, -8);
	plot.draw_line(-13, 0);
	plot.draw_line(0, -4);
	plot.draw_line(13, 0);
	plot.draw_line(1, -7);
	plot.draw_line(-13, 0);
	plot.draw_line(0, -4);
	plot.draw_line(21, 0);
	plot.draw_line(-4, 23);
	plot.draw_line(9, 0);
	plot.draw_line(4, -23);
	plot.draw_line(8, 0);
	plot.draw_line(-4, 23);
	plot.draw_line(9, 0);
	plot.draw_line(2, -12);
	plot.draw_line(6, 0);
	plot.draw_line(-2, 12);
	plot.draw_line(9, 0);
	plot.draw_line(6, -31);
	plot.draw_line(-9, 0);
	plot.draw_line(-2, 12);
	up();

    up();
    plot.drawline(40, -8);
    down();
	plot.draw_line(3, 0);
	plot.draw_line(0, -4);
	plot.draw_line(-3, 0);
	plot.draw_line(0, 4);
	up();

    up();
    plot.drawline(8, 0);
    down();
	plot.draw_line(3, 0);
	plot.draw_line(0, -4);
	plot.draw_line(-3, 0);
	plot.draw_line(0, 4);
	up();

    up();
    plot.drawline(29, 0);
    down();
	plot.draw_line(3, 0);
	plot.draw_line(0, -4);
	plot.draw_line(-3, 0);
	plot.draw_line(0, 4);
	up();

    up();
    plot.drawline(15, 5);
    down();
	plot.bezier_c(159, 9, 155, 13, 154, 20);
	plot.bezier_c(153, 28, 156, 31, 161, 31);
	plot.draw_line(0, 0);
	plot.draw_line(-1, -2);
	plot.draw_line(0, 0);
	plot.draw_line(0, 0);
	plot.bezier_c(159, 28, 157, 27, 157, 23);
	plot.draw_line(0, 0);
	plot.draw_line(2, -1);
	plot.draw_line(0, 0);
	plot.draw_line(0, 0);
	plot.draw_line(0, 0);
	up();

    up();
    plot.drawline(20, 0);
    down();
	plot.draw_line(2, -11);
	plot.draw_line(-3, 0);
	plot.draw_line(-6, 31);
	plot.draw_line(3, 0);
	plot.draw_line(2, -13);
	plot.bezier_c(179, 12, 183, 12, 184, 12);
	plot.draw_line(-2, 13);
	plot.draw_line(3, 0);
	plot.draw_line(2, -13);
	plot.draw_line(0, 0);
	up();

    up();
    plot.drawline(-41, 21);
    down();
	plot.draw_line(0, 0);
	plot.draw_line(3, 0);
	plot.draw_line(4, -21);
	plot.draw_line(-2, 0);
	plot.draw_line(-4, 20);
	up();

    up();
    plot.drawline(-55, -18);
    down();
	plot.draw_line(0, 0);
	plot.draw_line(10, 0);
	plot.draw_line(-13, 15);
	plot.draw_line(0, 0);
	plot.draw_line(0, 2);
	plot.draw_line(14, 0);
	plot.draw_line(0, -3);
	plot.draw_line(-10, 0);
	plot.draw_line(13, -15);
	plot.draw_line(0, 0);
	plot.draw_line(0, -2);
	plot.draw_line(-14, 0);
	plot.draw_line(0, 2);
	up();

    up();
    plot.drawline(50, -3);
    down();
	plot.draw_line(0, -2);
	plot.draw_line(0, 0);
	plot.draw_line(-3, 0);
	plot.draw_line(-4, 20);
	plot.draw_line(0, 0);
	plot.draw_line(3, 0);
	plot.draw_line(2, -12);
	plot.bezier_c(132, 14, 135, 12, 137, 12);
	plot.draw_line(0, 0);
	plot.draw_line(2, -2);
	plot.draw_line(0, 0);
	plot.draw_line(0, 0);
	up();

    up();
    plot.drawline(-18, 0);
    down();
	plot.draw_line(3, 0);
	plot.draw_line(0, 0);
	plot.draw_line(-4, 20);
	plot.draw_line(-3, 0);
	plot.draw_line(0, 0);
	plot.draw_line(0, -2);
	plot.draw_line(0, 0);
	plot.draw_line(2, -13);
	plot.draw_line(3, 0);
	plot.draw_line(0, 0);
	plot.draw_line(-2, 12);
	plot.bezier_c(112, 28, 116, 28, 117, 22);
	plot.draw_line(2, -12);
	up();
}

void loop() {}