import pwm_dac as pwm
import signal_generator as sg
import time

# Задаем параметры сигнала согласно графикам из методички
amplitude = 2.0              # Амплитуда сигнала 2.0 В
signal_frequency = 10        # Частота сигнала 10 Гц
sampling_frequency = 1000    # Частота дискретизации 1000 Гц

try:
    # Создаем объект класса для управления ЦАП на ШИМ
    # (GPIO пин 12, частота ШИМ 500 Гц, динамический диапазон 3.29 В)
    dac = pwm.PWM_DAC(12, 500, 3.290, verbose=False)
    
    start_time = time.time()
    
    while True:
        # Вычисляем текущее время работы скрипта
        current_time = time.time() - start_time
        
        # Получаем нормализованную амплитуду (от 0 до 1)
        normalized_amplitude = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        
        # Масштабируем до нужного напряжения
        voltage = normalized_amplitude * amplitude
        
        # Подаем напряжение на пин OUT блока PWM DAC
        dac.set_voltage(voltage)
        
        # Ждем один период дискретизации
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # Останавливаем ШИМ и очищаем настройки GPIO при завершении
    dac.deinit()