import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
button = 13
foto = 6
state = 0
GPIO.setup(led, GPIO.OUT)
GPIO.setup(foto, GPIO.IN)

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.15)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0
