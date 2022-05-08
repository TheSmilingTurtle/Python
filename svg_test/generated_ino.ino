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

   delay(200)
}

void up()
{
    for (; agl >= 135; --agl)
    {
    servo.write(agl);
    delay(15);
    }

    delay(200)
}

void setup()
{
    servo.attach(6);

    up();

    up();
    delay(200);
    plot.draw_line(711, 528);
    down();
	delay(200);
	plot.draw_line(-267, 267);
	delay(200);
	plot.draw_line(-267, -267);
	delay(200);
	plot.draw_line(267, -267);
	delay(200);
	plot.draw_line(267, 267);
	delay(200);
	plot.draw_line(0, 0);
	up();
}

void loop() {}