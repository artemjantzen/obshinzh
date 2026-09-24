import RPi.GPIO as GPIO
import time
import math

PIN = 12

GPIO.setmode(GPIO.BCM) 
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, 1000)
pwm.start(0)

alfa = 100
sine_table = []

for i in range(alfa):
    sin_val = math.sin(2 * math.pi * i / alfa)
    duty = (sin_val + 1) / 2 * 100.0
    sine_table.append(duty)

try:
    while True:
        for duty in sine_table:
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.01)
            
except:
    pass