import r2r_dac as r2r #[cite: 23]
import signal_generator as sg #[cite: 23]
import time #[cite: 23]

# Переменные для хранения параметров генерируемого сигнала[cite: 23]
amplitude = 3.2 #[cite: 23]
signal_frequency = 10 #[cite: 23]
sampling_frequency = 1000 #[cite: 23]

try:
    # Создается объект класса для управления R2R-ЦАП[cite: 23]
    # (Используются параметры инициализации из предыдущих заданий)
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.29, verbose=False)
    
    start_time = time.time()
    
    while True:
        # В бесконечном цикле генерируется сигнал при помощи функций из модуля signal_generator[cite: 23]
        current_time = time.time() - start_time
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude * amplitude
        
        # Подается напряжение на пин OUT блока 8-bit DAC[cite: 23]
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # Вызывается «деструктор» объекта класса управления R2R-ЦАП[cite: 23]
    dac.deinit()