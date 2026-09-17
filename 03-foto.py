import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
button = 13
foto = 6
state = 0
GPIO.setup(led, GPIO.OUT)
GPIO.setup(foto, GPIO.IN)

while True:
    if GPIO.input(foto):
        state = foto.value()
        GPIO.output(led, not state)
        time.sleep(0.5)