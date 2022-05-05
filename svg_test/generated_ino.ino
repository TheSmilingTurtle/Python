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
    plot.drawline(351, 60);
    down();
	plot.draw_line(-35, 0);
	plot.draw_line(12, -60);
	plot.draw_line(-293, 0);
	plot.draw_line(-31, 155);
	plot.draw_line(117, 0);
	plot.draw_line(8, -40);
	plot.draw_line(-69, 0);
	plot.draw_line(4, -20);
	plot.draw_line(69, 0);
	plot.draw_line(7, -35);
	plot.draw_line(-69, 0);
	plot.draw_line(4, -20);
	plot.draw_line(110, 0);
	plot.draw_line(-23, 115);
	plot.draw_line(48, 0);
	plot.draw_line(23, -115);
	plot.draw_line(40, 0);
	plot.draw_line(-23, 115);
	plot.draw_line(48, 0);
	plot.draw_line(12, -60);
	plot.draw_line(35, 0);
	plot.draw_line(-12, 60);
	plot.draw_line(48, 0);
	plot.draw_line(31, -155);
	plot.draw_line(-48, 0);
	plot.draw_line(-12, 60);
	up();
}

void loop() {}