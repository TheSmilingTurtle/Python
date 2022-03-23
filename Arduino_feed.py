import serial

var = b''

Serial = serial.Serial(
    port="COM3",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)    

while (True):
    send = bytes(input("Input: "), "UTF-8")
    Serial.write(send)
    while (Serial.read()):
        temp = Serial.read()
        if (temp != b'\n'):
            var += temp

    print(var)