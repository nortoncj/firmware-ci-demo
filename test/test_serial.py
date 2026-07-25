import serial

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=5)

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if line:
        print(line)