import r2r_dac as r2r 
import signal_generator as sg 
import time 

# Параметры сигнала, которые можно задавать в скрипте[cite: 24]
amplitude = 2.0 # Амплитуда 2.0 В, как на графике[cite: 25]
signal_frequency = 10 # Частота 10 Гц, как на графике[cite: 25]
sampling_frequency = 1000 

try:
    # Инициализация объекта для управления R2R-ЦАП
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.29, verbose=False)
    
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        
        # Получение нормализованной амплитуды треугольного сигнала
        normalized_amplitude = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude * amplitude
        
        # Вывод напряжения на пин OUT[cite: 24]
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # Сброс настроек
    dac.deinit()