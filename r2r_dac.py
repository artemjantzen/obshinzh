import RPi.GPIO as GPIO #[cite: 10]

class R2R_DAC: #[cite: 10]
    def __init__(self, gpio_bits, dynamic_range, verbose = False): #[cite: 10]
        self.gpio_bits = gpio_bits #[cite: 10]
        self.dynamic_range = dynamic_range #[cite: 10]
        self.verbose = verbose #[cite: 10]
        GPIO.setmode(GPIO.BCM) #[cite: 10]
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0) #[cite: 10]

    def deinit(self): #[cite: 10]
        GPIO.output(self.gpio_bits, 0) #[cite: 10]
        GPIO.cleanup() #[cite: 10]
        
    def set_number(self, number):
        # Принимает на вход целое число и подаёт его двоичное представление на вход R2R-ЦАП[cite: 11]
        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {bits}") #[cite: 8]
        for i in range(8):
            GPIO.output(self.gpio_bits[i], bits[i])
            
    def set_voltage(self, voltage):
        # Метод принимает на вход вещественное число и подаёт его двоичное представление на вход R2R-ЦАП при помощи метода set_number[cite: 11]
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)") #[cite: 8]
            voltage = 0.0
        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number) #[cite: 11]

if __name__ == "__main__": #[cite: 11]
    try: #[cite: 11]
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True) #[cite: 11]
        while True: #[cite: 11]
            try: #[cite: 11]
                voltage = float(input("Введите напряжение в Вольтах: ")) #[cite: 11]
                dac.set_voltage(voltage) #[cite: 11]
            except ValueError: #[cite: 11]
                print("Вы ввели не число. Попробуйте ещё раз\n") #[cite: 11]
    finally: #[cite: 11]
        dac.deinit() #[cite: 11]