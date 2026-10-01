import mcp4725_driver as mcp
import signal_generator as sg
import time

# Задаем параметры сигнала согласно графикам из методички
amplitude = 2.0              # Амплитуда сигнала 2.0 В
signal_frequency = 10        # Частота сигнала 10 Гц
sampling_frequency = 1000    # Частота дискретизации 1000 Гц

try:
    # Создаем объект класса для управления микросхемой MCP4725 по I2C
    # (динамический диапазон 5.11 В, адрес 0x61)
    dac = mcp.MCP4725(5.11, 0x61, verbose=False)
    
    start_time = time.time()
    
    while True:
        # Вычисляем текущее время работы скрипта
        current_time = time.time() - start_time
        
        # Получаем нормализованную амплитуду (от 0 до 1)
        normalized_amplitude = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        
        # Масштабируем до нужного напряжения
        voltage = normalized_amplitude * amplitude
        
        # Подаем напряжение на пин OUT блока 12-bit DAC
        dac.set_voltage(voltage)
        
        # Ждем один период дискретизации
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # Обязательно освобождаем шину I2C при завершении (в т.ч. по Ctrl+C)
    dac.deinit()