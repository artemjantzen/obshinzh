import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
#led = 26
button = 13
num = 0
up, down = 9, 10
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.output(leds, 0)

while True:
    if GPIO.input(up) and GPIO.input(down):
        num = 256
    elif GPIO.input(up) and not GPIO.input(down):
        if (num < 255):
            num = num + 1
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
    elif GPIO.input(down) and not GPIO.input(up):
        if (num > 0):
            num = num - 1
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
    time.sleep(0.1)
