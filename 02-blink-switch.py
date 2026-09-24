import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
button = 13
state = 0
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)