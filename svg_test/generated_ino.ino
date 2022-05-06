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

   delay(200)
}

void up()
{
    for (; agl >= 120; --agl)
    {
    servo.write(agl);
    delay(15);
    }

    delay(200)
}

void setup()
{
    servo.attach(4);

    up();

    up();
    plot.drawline(1545, 937);
    down();
	plot.draw_line(116, 0);
	plot.draw_line(0, 129);
	plot.bezier_c(1713, 990, 1771, 953);
	plot.bezier_c(1829, 914, 1891, 914);
	plot.bezier_c(1939, 914, 1992, 944);
	plot.draw_line(-59, 96);
	plot.bezier_c(1897, 1025, 1873, 1025);
	plot.bezier_c(1816, 1025, 1763, 1072);
	plot.bezier_c(1710, 1119, 1682, 1217);
	plot.bezier_c(1661, 1293, 1661, 1523);
	plot.draw_line(0, 299);
	plot.draw_line(-116, 0);
	plot.draw_line(0, -885);
	up();

    up();
    plot.drawline(399, -115);
    down();
	plot.draw_line(53, 0);
	plot.draw_line(18, -49);
	plot.bezier_c(2031, 769, 2046, 764, 2060, 755);
	plot.draw_line(0, 0);
	plot.draw_line(48, 23);
	plot.draw_line(37, -38);
	plot.draw_line(-23, -48);
	plot.draw_line(0, 0);
	plot.bezier_c(2131, 679, 2136, 664, 2140, 647);
	plot.draw_line(49, -18);
	plot.draw_line(0, -54);
	plot.draw_line(-49, -18);
	plot.bezier_c(2136, 542, 2130, 526, 2122, 512);
	plot.draw_line(0, 0);
	plot.draw_line(23, -48);
	plot.draw_line(-37, -38);
	plot.draw_line(-48, 23);
	plot.draw_line(0, 0);
	plot.bezier_c(2046, 441, 2031, 432, 2014, 428);
	plot.draw_line(-18, -52);
	plot.draw_line(-53, 0);
	plot.draw_line(-18, 52);
	plot.bezier_c(1910, 432, 1895, 440, 1881, 448);
	plot.draw_line(0, 0);
	plot.draw_line(-48, -23);
	plot.draw_line(-37, 38);
	plot.draw_line(23, 48);
	plot.draw_line(0, 0);
	plot.bezier_c(1810, 526, 1802, 542, 1798, 558);
	plot.draw_line(-51, 18);
	plot.draw_line(0, 54);
	plot.draw_line(51, 18);
	plot.bezier_c(1802, 664, 1809, 679, 1818, 693);
	plot.draw_line(0, 0);
	plot.draw_line(-22, 48);
	plot.draw_line(38, 38);
	plot.draw_line(48, -23);
	plot.draw_line(0, 0);
	plot.bezier_c(1895, 765, 1910, 769, 1926, 774);
	plot.draw_line(18, 49);
	up();

    up();
    plot.drawline(-62, -220);
    down();
	plot.bezier_c(1882, 553, 1922, 513, 1970, 513);
	plot.bezier_c(2019, 513, 2059, 553, 2059, 603);
	plot.bezier_c(2059, 652, 2019, 692, 1970, 692);
	plot.bezier_c(1922, 692, 1882, 652, 1882, 603);
	plot.draw_line(0, 0);
	up();

    up();
    plot.drawline(403, 416);
    down();
	plot.draw_line(31, -13);
	plot.draw_line(-2, -33);
	plot.bezier_c(2323, 966, 2331, 959, 2337, 950);
	plot.draw_line(0, 0);
	plot.draw_line(33, 2);
	plot.draw_line(13, -31);
	plot.draw_line(-25, -22);
	plot.draw_line(0, 0);
	plot.bezier_c(2360, 888, 2360, 878, 2358, 867);
	plot.draw_line(25, -22);
	plot.draw_line(-13, -31);
	plot.draw_line(-33, 2);
	plot.bezier_c(2331, 807, 2323, 800, 2315, 794);
	plot.draw_line(0, 0);
	plot.draw_line(2, -33);
	plot.draw_line(-31, -13);
	plot.draw_line(-22, 25);
	plot.draw_line(0, 0);
	plot.bezier_c(2253, 771, 2242, 770, 2232, 772);
	plot.draw_line(-22, -25);
	plot.draw_line(-31, 13);
	plot.draw_line(2, 34);
	plot.bezier_c(2171, 800, 2164, 807, 2158, 816);
	plot.draw_line(0, 0);
	plot.draw_line(-33, -2);
	plot.draw_line(-13, 34);
	plot.draw_line(25, 25);
	plot.draw_line(0, 0);
	plot.bezier_c(2135, 880, 2135, 891, 2136, 902);
	plot.draw_line(-25, 21);
	plot.draw_line(13, 30);
	plot.draw_line(33, -2);
	plot.bezier_c(2164, 959, 2172, 966, 2180, 973);
	plot.draw_line(0, 0);
	plot.draw_line(-2, 33);
	plot.draw_line(31, 13);
	plot.draw_line(22, -25);
	plot.draw_line(0, 0);
	plot.bezier_c(2242, 995, 2252, 995, 2263, 994);
	plot.draw_line(22, 25);
	up();

    up();
    plot.drawline(-90, -114);
    down();
	plot.bezier_c(2184, 876, 2197, 843, 2226, 831);
	plot.bezier_c(2255, 819, 2287, 833, 2299, 862);
	plot.bezier_c(2311, 890, 2297, 923, 2269, 935);
	plot.bezier_c(2240, 947, 2207, 933, 2196, 904);
	plot.draw_line(0, 0);
	up();
}

void loop() {}