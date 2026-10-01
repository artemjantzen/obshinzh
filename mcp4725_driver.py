import smbus #[cite: 15]

class MCP4725: #[cite: 15]
    def __init__(self, dynamic_range, address=0x61, verbose=True): #[cite: 15]
        self.bus = smbus.SMBus(1) #[cite: 15]
        self.address = address #[cite: 15]
        self.wm = 0x00 #[cite: 15]
        self.pds = 0x00 #[cite: 15]
        self.verbose = verbose #[cite: 15]
        self.dynamic_range = dynamic_range #[cite: 15]

    def deinit(self): #[cite: 15]
        self.bus.close() #[cite: 15]

    def set_number(self, number): #[cite: 15]
        if not isinstance(number, int): #[cite: 15]
            print("На вход ЦАП можно подавать только целые числа") #[cite: 15]
            return
        if not (0 <= number <= 4095): #[cite: 15]
            print("Число выходит за разраядность MCP4752 (12 бит)") #[cite: 15]
            return
        first_byte = self.wm | self.pds | (number >> 8) #[cite: 15]
        second_byte = number & 0xFF #[cite: 15]
        self.bus.write_byte_data(0x61, first_byte, second_byte) #[cite: 15]
        if self.verbose: #[cite: 15]
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n") #[cite: 15]

    def set_voltage(self, voltage): #[cite: 15]
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)") #[cite: 12]
            voltage = 0.0
        number = int((voltage / self.dynamic_range) * 4095)
        self.set_number(number)

if __name__ == "__main__": #
    try: #
        dac = MCP4725(5.11, 0x61, True) #[cite: 12, 15]
        while True: #
            try: #[cite: 16]
                voltage = float(input("Введите напряжение в Вольтах: ")) #[cite: 12]
                dac.set_voltage(voltage) #[cite: 12]
            except ValueError: #[cite: 16]
                print("Вы ввели не число. Попробуйте ещё раз\n") #[cite: 12]
    finally: #[cite: 16]
        dac.deinit() #[cite: 12]