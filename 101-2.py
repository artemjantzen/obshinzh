import RPi.GPIO as GPIO
import time

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= 3.3):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / 3.3 * 100)

GPIO.setmode(GPIO.BCM)
PWM_PIN = 12
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm_output = GPIO.PWM(PWM_PIN, 1000)

pwm_output.start(0)

while True:
    try:
        voltage = float(input("Введите напряжение в Вольтах: "))
        number = voltage_to_number(voltage)
        pwm_output.ChangeDutyCycle(number)
    except:
        pass
