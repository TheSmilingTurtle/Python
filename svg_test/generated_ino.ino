#include <PlotterV3.h>
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

   delay(200);
}

void up()
{
    for (; agl >= 135; --agl)
    {
    servo.write(agl);
    delay(15);
    }

    delay(200);
}

void setup()
{
    servo.attach(_SERVO);

    up();
    plot.calibrate();
    

    up();
    delay(200);
    plot.draw_line(568, 547);
    down();
	delay(200);
	plot.draw_line(-61, 0);
	delay(200);
	plot.bezier_c(510, 510, 522, 450, 560, 379);
	delay(200);
	plot.bezier_c(604, 299, 607, 219, 568, 153);
	delay(200);
	plot.bezier_c(525, 82, 438, 37, 346, 38);
	delay(200);
	plot.draw_line(-1, 0);
	delay(200);
	plot.bezier_c(253, 37, 167, 82, 124, 153);
	delay(200);
	plot.bezier_c(85, 219, 87, 299, 131, 379);
	delay(200);
	plot.bezier_c(170, 450, 182, 510, 185, 548);
	delay(200);
	plot.draw_line(-62, 0);
	delay(200);
	plot.draw_line(-28, -61);
	delay(200);
	plot.draw_line(-95, 44);
	delay(200);
	plot.draw_line(56, 122);
	delay(200);
	plot.draw_line(224, 2);
	delay(200);
	plot.draw_line(8, -44);
	delay(200);
	plot.bezier_c(289, 605, 309, 484, 223, 329);
	delay(200);
	plot.bezier_c(197, 281, 194, 240, 214, 207);
	delay(200);
	plot.bezier_c(237, 169, 291, 143, 344, 143);
	delay(200);
	plot.draw_line(0, 0);
	delay(200);
	plot.draw_line(3, 0);
	delay(200);
	plot.bezier_c(401, 143, 455, 169, 478, 207);
	delay(200);
	plot.bezier_c(498, 240, 494, 281, 468, 329);
	delay(200);
	plot.bezier_c(383, 484, 403, 605, 404, 610);
	delay(200);
	plot.draw_line(8, 44);
	delay(200);
	plot.draw_line(224, -2);
	delay(200);
	plot.draw_line(56, -122);
	delay(200);
	plot.draw_line(-95, -44);
	delay(200);
	plot.draw_line(-28, 61);
	up();
}

void loop() {}