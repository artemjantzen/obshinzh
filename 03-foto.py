import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
foto = 6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(foto, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(foto))
    time.sleep(0.5)