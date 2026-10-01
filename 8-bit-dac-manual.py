import RPi.GPIO as GPIO #[cite: 4]

# Пины заданы согласно второму заданию методички
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22] #
dynamic_range = 3.17 #[cite: 2]

GPIO.setmode(GPIO.BCM) #[cite: 10]
GPIO.setup(dac_bits, GPIO.OUT, initial=0) #[cite: 10]

def voltage_to_number(voltage):
    # Перед возвратом целого числа функция проверят, что напряжение укладывается в динамический диапазон ЦАП[cite: 5]
    if not (0.0 <= voltage <= dynamic_range): #[cite: 4]
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)") #[cite: 4]
        print("Устанавлниваем 0.0 В") #[cite: 4]
        return 0 #[cite: 4]
    return int(voltage / dynamic_range * 255) #[cite: 4]

def number_to_dac(number):
    # Функция number_to_dac(number) принимает на вход целое число и подаёт его двоичное представление на вход R2R-ЦАП[cite: 5]
    bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
    print(f"Число на вход ЦАП: {number}, биты: {bits}") #[cite: 2]
    for i in range(8):
        GPIO.output(dac_bits[i], bits[i])

try: #[cite: 5]
    while True: #[cite: 5]
        try: #[cite: 5]
            voltage = float(input("Введите напряжение в Вольтах: ")) #[cite: 5]
            number = voltage_to_number(voltage) #[cite: 5]
            number_to_dac(number) #[cite: 5]
        except ValueError: #[cite: 5]
            print("Вы ввели не число. Попробуйте ещё раз\n") #[cite: 5]
finally: #[cite: 5]
    GPIO.output(dac_bits, 0) #[cite: 5]
    GPIO.cleanup() #[cite: 5]