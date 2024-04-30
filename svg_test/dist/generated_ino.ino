#include <PlotterV5.h>
#include <Servo.h>

Plt plot = Plt();
Servo servo;

int agl = 170;

void down()
{
    for (; agl <= 160; ++agl)
    {
    servo.write(agl);
    delay(15);
    }

    delay(100);
}

void up()
{
    for (; agl >= 140; --agl)
    {
    servo.write(agl);
    delay(15);
    }

    delay(100);
}

void setup()
{
    servo.attach(_SERVO);

    up();
    plot.calibrate();
    

    up();
    delay(100);
    plot.draw_line(135, 19);
    down();
	delay(100);
	plot.bezier_c(173, 22, 178, 25, 178, 47);
	delay(100);
	plot.bezier_c(104, 50, 0, 84, 0, 193);
	delay(100);
	plot.bezier_c(0, 303, 106, 342, 178, 343);
	delay(100);
	plot.bezier_c(178, 370, 173, 373, 135, 376);
	delay(100);
	plot.draw_line(0, 19);
	delay(100);
	plot.draw_line(136, 0);
	delay(100);
	plot.draw_line(0, -19);
	delay(100);
	plot.bezier_c(233, 373, 229, 370, 229, 343);
	delay(100);
	plot.bezier_c(298, 342, 406, 306, 406, 197);
	delay(100);
	plot.bezier_c(406, 89, 302, 50, 229, 47);
	delay(100);
	plot.bezier_c(229, 25, 233, 22, 268, 19);
	delay(100);
	plot.draw_line(0, -19);
	delay(100);
	plot.draw_line(-133, 0);
	delay(100);
	plot.draw_line(0, 19);

    up();
    delay(100);
    plot.draw_line(94, 50);
    down();
	delay(100);
	plot.bezier_c(280, 72, 349, 101, 349, 192);
	delay(100);
	plot.bezier_c(349, 285, 281, 317, 229, 321);
	delay(100);
	plot.draw_line(0, -251);

    up();
    delay(100);
    plot.draw_line(-51, 251);
    down();
	delay(100);
	plot.bezier_c(127, 317, 56, 288, 56, 195);
	delay(100);
	plot.bezier_c(56, 101, 127, 72, 178, 70);
	delay(100);
	plot.draw_line(0, 251);
	up();
}

void loop() {}