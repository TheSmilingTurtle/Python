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

    up();
    plot.drawline(862, 1682);
    down();
	plot.draw_line(233, 0);
	plot.draw_line(0, 259);
	plot.bezier_c(1199, 1787, 1314, 1713);
	plot.bezier_c(1430, 1636, 1555, 1636);
	plot.bezier_c(1649, 1636, 1757, 1696);
	plot.draw_line(-119, 192);
	plot.bezier_c(1566, 1857, 1518, 1857);
	plot.bezier_c(1404, 1857, 1298, 1952);
	plot.bezier_c(1192, 2045, 1137, 2241);
	plot.bezier_c(1094, 2393, 1094, 2853);
	plot.draw_line(0, 599);
	plot.draw_line(-233, 0);
	plot.draw_line(0, -1771);
	up();

    up();
    plot.drawline(-1027, -2709);
    down();
	plot.draw_line(0, -71);
	plot.draw_line(-65, -24);
	plot.bezier_c(625, 537, 618, 517, 607, 498);
	plot.draw_line(1, 0);
	plot.draw_line(31, -64);
	plot.draw_line(-50, -51);
	plot.draw_line(-64, 31);
	plot.draw_line(0, 0);
	plot.bezier_c(505, 402, 484, 395, 462, 390);
	plot.draw_line(-24, -66);
	plot.draw_line(-71, 0);
	plot.draw_line(-24, 66);
	plot.bezier_c(321, 395, 301, 403, 282, 414);
	plot.draw_line(0, 0);
	plot.draw_line(-64, -31);
	plot.draw_line(-51, 50);
	plot.draw_line(31, 64);
	plot.draw_line(0, 0);
	plot.bezier_c(186, 517, 175, 537, 170, 559);
	plot.draw_line(-70, 24);
	plot.draw_line(0, 71);
	plot.draw_line(70, 24);
	plot.bezier_c(175, 700, 185, 721, 196, 740);
	plot.draw_line(0, 0);
	plot.draw_line(-30, 64);
	plot.draw_line(51, 51);
	plot.draw_line(64, -31);
	plot.draw_line(0, 0);
	plot.bezier_c(301, 835, 321, 845, 343, 851);
	plot.draw_line(24, 69);
	plot.draw_line(71, 0);
	plot.draw_line(24, -69);
	plot.bezier_c(484, 845, 505, 836, 524, 825);
	plot.draw_line(0, 0);
	plot.draw_line(64, 30);
	plot.draw_line(51, -51);
	plot.draw_line(-31, -64);
	plot.draw_line(0, 0);
	plot.bezier_c(619, 721, 625, 700, 631, 678);
	plot.draw_line(65, -24);
	up();

    up();
    plot.drawline(-989, -571);
    down();
	plot.bezier_c(337, 738, 284, 684, 284, 619);
	plot.bezier_c(284, 553, 337, 500, 403, 500);
	plot.bezier_c(468, 500, 522, 553, 522, 619);
	plot.bezier_c(522, 684, 468, 738, 403, 738);
	plot.draw_line(0, 0);
	up();

    up();
    plot.drawline(119, -1253);
    down();
	plot.draw_line(-16, -38);
	plot.draw_line(-40, 2);
	plot.bezier_c(861, 176, 852, 167, 842, 160);
	plot.draw_line(0, 0);
	plot.draw_line(2, -41);
	plot.draw_line(-38, -16);
	plot.draw_line(-27, 30);
	plot.draw_line(0, 0);
	plot.bezier_c(766, 132, 754, 132, 741, 134);
	plot.draw_line(-27, -30);
	plot.draw_line(-38, 16);
	plot.draw_line(2, 41);
	plot.bezier_c(668, 168, 659, 177, 651, 187);
	plot.draw_line(0, 0);
	plot.draw_line(-41, -2);
	plot.draw_line(-16, 38);
	plot.draw_line(30, 27);
	plot.draw_line(0, 0);
	plot.bezier_c(624, 261, 623, 275, 625, 288);
	plot.draw_line(-30, 27);
	plot.draw_line(16, 38);
	plot.draw_line(41, -2);
	plot.bezier_c(659, 361, 668, 370, 678, 377);
	plot.draw_line(0, 0);
	plot.draw_line(-2, 41);
	plot.draw_line(41, 16);
	plot.draw_line(31, -30);
	plot.draw_line(0, 0);
	plot.bezier_c(756, 405, 770, 405, 782, 403);
	plot.draw_line(25, 30);
	plot.draw_line(37, -16);
	plot.draw_line(-3, -41);
	plot.bezier_c(852, 370, 861, 361, 869, 350);
	plot.draw_line(0, 0);
	plot.draw_line(41, 2);
	plot.draw_line(16, -38);
	plot.draw_line(-30, -27);
	plot.draw_line(0, 0);
	plot.bezier_c(896, 275, 896, 262, 894, 250);
	plot.draw_line(30, -27);
	up();

    up();
    plot.drawline(-1063, -113);
    down();
	plot.bezier_c(751, 346, 711, 329, 697, 295);
	plot.bezier_c(683, 260, 699, 220, 734, 206);
	plot.bezier_c(768, 191, 808, 208, 823, 243);
	plot.bezier_c(837, 277, 821, 317, 786, 331);
	plot.draw_line(0, 0);
	up();
}

void loop() {}