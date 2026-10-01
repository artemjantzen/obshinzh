import pwm_dac as pwm #[cite: 20]
import signal_generator as sg #[cite: 20]
import time #[cite: 20]

# Создаются переменные для хранения параметров генерируемого сигнала[cite: 20]
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    # Создается объект класса для управления ЦАП на ШИМ[cite: 20]
    # (Параметры: пин 12, частота 500 Гц, динамический диапазон 3.29В)
    dac = pwm.PWM_DAC(12, 500, 3.290, verbose=False) 
    
    start_time = time.time()
    
    while True:
        # В бесконечном цикле генерируется сигнал[cite: 20]
        current_time = time.time() - start_time
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude * amplitude
        
        # Подается напряжение на пин OUT блока PWM DAC[cite: 20]
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # Вызывается «деструктор» объекта класса управления ЦАП на ШИМ[cite: 20]
    dac.deinit()