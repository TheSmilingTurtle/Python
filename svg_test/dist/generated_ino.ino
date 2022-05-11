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
    plot.draw_line(2383, 937);
    down();
	delay(100);
	plot.draw_line(-116, 0);
	delay(100);
	plot.draw_line(0, 129);
	delay(100);
	plot.bezier_q(2215, 990, 2157, 953);
	delay(100);
	plot.bezier_q(2099, 914, 2037, 914);
	delay(100);
	plot.bezier_q(1989, 914, 1936, 944);
	delay(100);
	plot.draw_line(59, 96);
	delay(100);
	plot.bezier_q(2031, 1025, 2055, 1025);
	delay(100);
	plot.bezier_q(2112, 1025, 2165, 1072);
	delay(100);
	plot.bezier_q(2218, 1119, 2246, 1217);
	delay(100);
	plot.bezier_q(2267, 1293, 2267, 1523);
	delay(100);
	plot.draw_line(0, 299);
	delay(100);
	plot.draw_line(116, 0);
	delay(100);
	plot.draw_line(0, -885);

    up();
    delay(100);
    plot.draw_line(-399, -115);
    down();
	delay(100);
	plot.draw_line(-53, 0);
	delay(100);
	plot.draw_line(-18, -49);
	delay(100);
	plot.bezier_c(1897, 769, 1882, 764, 1868, 755);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(-48, 23);
	delay(100);
	plot.draw_line(-37, -38);
	delay(100);
	plot.draw_line(23, -48);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(1797, 679, 1792, 664, 1788, 647);
	delay(100);
	plot.draw_line(-49, -18);
	delay(100);
	plot.draw_line(0, -54);
	delay(100);
	plot.draw_line(49, -18);
	delay(100);
	plot.bezier_c(1792, 542, 1798, 526, 1806, 512);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(-23, -48);
	delay(100);
	plot.draw_line(37, -38);
	delay(100);
	plot.draw_line(48, 23);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(1882, 441, 1897, 432, 1914, 428);
	delay(100);
	plot.draw_line(18, -52);
	delay(100);
	plot.draw_line(53, 0);
	delay(100);
	plot.draw_line(18, 52);
	delay(100);
	plot.bezier_c(2018, 432, 2033, 440, 2047, 448);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(48, -23);
	delay(100);
	plot.draw_line(37, 38);
	delay(100);
	plot.draw_line(-23, 48);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(2118, 526, 2126, 542, 2130, 558);
	delay(100);
	plot.draw_line(51, 18);
	delay(100);
	plot.draw_line(0, 54);
	delay(100);
	plot.draw_line(-51, 18);
	delay(100);
	plot.bezier_c(2126, 664, 2119, 679, 2110, 693);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(22, 48);
	delay(100);
	plot.draw_line(-38, 38);
	delay(100);
	plot.draw_line(-48, -23);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(2033, 765, 2018, 769, 2002, 774);
	delay(100);
	plot.draw_line(-18, 49);

    up();
    delay(100);
    plot.draw_line(62, -220);
    down();
	delay(100);
	plot.bezier_c(2046, 553, 2006, 513, 1958, 513);
	delay(100);
	plot.bezier_c(1909, 513, 1869, 553, 1869, 603);
	delay(100);
	plot.bezier_c(1869, 652, 1909, 692, 1958, 692);
	delay(100);
	plot.bezier_c(2006, 692, 2046, 652, 2046, 603);
	delay(100);
	plot.draw_line(0, 0);

    up();
    delay(100);
    plot.draw_line(-403, 416);
    down();
	delay(100);
	plot.draw_line(-31, -13);
	delay(100);
	plot.draw_line(2, -33);
	delay(100);
	plot.bezier_c(1605, 966, 1597, 959, 1591, 950);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(-33, 2);
	delay(100);
	plot.draw_line(-13, -31);
	delay(100);
	plot.draw_line(25, -22);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(1568, 888, 1568, 878, 1570, 867);
	delay(100);
	plot.draw_line(-25, -22);
	delay(100);
	plot.draw_line(13, -31);
	delay(100);
	plot.draw_line(33, 2);
	delay(100);
	plot.bezier_c(1597, 807, 1605, 800, 1613, 794);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(-2, -33);
	delay(100);
	plot.draw_line(31, -13);
	delay(100);
	plot.draw_line(22, 25);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(1675, 771, 1686, 770, 1696, 772);
	delay(100);
	plot.draw_line(22, -25);
	delay(100);
	plot.draw_line(31, 13);
	delay(100);
	plot.draw_line(-2, 34);
	delay(100);
	plot.bezier_c(1757, 800, 1764, 807, 1770, 816);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(33, -2);
	delay(100);
	plot.draw_line(13, 34);
	delay(100);
	plot.draw_line(-25, 25);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(1793, 880, 1793, 891, 1792, 902);
	delay(100);
	plot.draw_line(25, 21);
	delay(100);
	plot.draw_line(-13, 30);
	delay(100);
	plot.draw_line(-33, -2);
	delay(100);
	plot.bezier_c(1764, 959, 1756, 966, 1748, 973);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.draw_line(2, 33);
	delay(100);
	plot.draw_line(-31, 13);
	delay(100);
	plot.draw_line(-22, -25);
	delay(100);
	plot.draw_line(0, 0);
	delay(100);
	plot.bezier_c(1686, 995, 1676, 995, 1665, 994);
	delay(100);
	plot.draw_line(-22, 25);

    up();
    delay(100);
    plot.draw_line(90, -114);
    down();
	delay(100);
	plot.bezier_c(1744, 876, 1731, 843, 1702, 831);
	delay(100);
	plot.bezier_c(1674, 819, 1641, 833, 1629, 862);
	delay(100);
	plot.bezier_c(1617, 890, 1631, 923, 1659, 935);
	delay(100);
	plot.bezier_c(1688, 947, 1721, 933, 1732, 904);
	delay(100);
	plot.draw_line(0, 0);
	up();
}

void loop() {}