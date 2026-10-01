import RPi.GPIO as GPIO #[cite: 18]

class PWM_DAC: #[cite: 18]
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False): #[cite: 18]
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM) #[cite: 16]
        GPIO.setup(self.gpio_pin, GPIO.OUT) #[cite: 16]
        self.pwm = GPIO.PWM(self.gpio_pin, pwm_frequency) #[cite: 16]
        self.pwm.start(0) #[cite: 16]

    def deinit(self): #[cite: 18]
        self.pwm.stop() #[cite: 16]
        GPIO.cleanup(self.gpio_pin) #[cite: 16]

    def set_voltage(self, voltage): #[cite: 18]
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)") #[cite: 16]
            voltage = 0.0
        duty_cycle = (voltage / self.dynamic_range) * 100
        if self.verbose:
            print(f"Коэффициент заполнения: {duty_cycle:.2f}") #[cite: 16]
        self.pwm.ChangeDutyCycle(duty_cycle) #[cite: 16]

if __name__ == "__main__": #[cite: 18]
    try: #[cite: 18]
        dac = PWM_DAC(12, 500, 3.290, True) #[cite: 18]
        while True: #[cite: 18]
            try: #[cite: 18]
                voltage = float(input("Введите напряжение в Вольтах: ")) #[cite: 18]
                dac.set_voltage(voltage) #[cite: 18]
            except ValueError: #[cite: 18]
                print("Вы ввели не число. Попробуйте ещё раз\n") #[cite: 18]
    finally: #[cite: 18]
        dac.deinit() #[cite: 18]