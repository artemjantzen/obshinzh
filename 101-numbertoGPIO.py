def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)
    
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
PWM_PIN = 6
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm_output = GPIO.PWM(PWM_PIN, 1000)

while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            pwm_output.ChangeDutyCycle(number)
    
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

pwm_output.stop()
GPIO.cleanup()
