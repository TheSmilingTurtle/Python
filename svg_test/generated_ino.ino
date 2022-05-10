#include <PlotterV4.h>
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
    plot.draw_line(124, 547);
    down();
	delay(100);
	plot.draw_line(61, 0);
	delay(100);
	plot.bezier_c(182, 510, 170, 450, 131, 379);
	delay(100);
	plot.bezier_c(87, 299, 85, 219, 124, 153);
	delay(100);
	plot.bezier_c(167, 82, 253, 37, 345, 38);
	delay(100);
	plot.draw_line(1, 0);
	delay(100);
	plot.bezier_c(438, 37, 525, 82, 568, 153);
	delay(100);
	plot.bezier_c(607, 219, 604, 299, 560, 379);
	delay(100);
	plot.bezier_c(521, 450, 510, 510, 507, 548);
	delay(100);
	plot.draw_line(62, 0);
	delay(100);
	plot.draw_line(28, -61);
	delay(100);
	plot.draw_line(95, 44);
	delay(100);
	plot.draw_line(-56, 122);
	delay(100);
	plot.draw_line(-224, 2);
	delay(100);
	plot.draw_line(-8, -44);
	delay(100);
	plot.bezier_c(403, 605, 383, 484, 468, 329);
	delay(100);
	plot.bezier_c(494, 281, 498, 240, 478, 207);
	delay(100);
	plot.bezier_c(455, 169, 401, 143, 347, 143);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(-3, 0);
	delay(100);
	plot.bezier_c(291, 143, 237, 169, 214, 207);
	delay(100);
	plot.bezier_c(194, 240, 197, 281, 223, 329);
	delay(100);
	plot.bezier_c(309, 484, 289, 605, 288, 610);
	delay(100);
	plot.draw_line(-8, 44);
	delay(100);
	plot.draw_line(-224, -2);
	delay(100);
	plot.draw_line(-56, -122);
	delay(100);
	plot.draw_line(95, -44);
	delay(100);
	plot.draw_line(28, 61);
	up();
}

void loop() {}