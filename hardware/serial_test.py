import serial
import time
import sys

port = "/dev/cu.usbserial-0001"
baud = 115200

ser = serial.Serial(port, baud, timeout=1)

# Give ESP32 time to reboot
time.sleep(2)

# Throw away any partial boot messages
ser.reset_input_buffer()

found_boot = False

start = time.time()

while time.time() - start < 10:

    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    print(line)

    if line == "BOOT OK":
        found_boot = True
        break

ser.close()

if found_boot:
    print("PASS")
    sys.exit(0)

print("FAIL")
sys.exit(1)