# Импортируются модули mcp4725_driver, signal_generator и модуль работы со временем[cite: 27]
import mcp4725_driver as mcp 
import signal_generator as sg 
import time 

# Создаются переменные для хранения параметров генерируемого сигнала[cite: 27]
amplitude = 3.333 
signal_frequency = 10 
sampling_frequency = 1000 

try:
    # В блоке try создается объект класса для управления микросхемой MCP4725 по I2C[cite: 27]
    dac = mcp.MCP4725(5.11, 0x61, verbose=False) 
    
    start_time = time.time()
    
    while True:
        # В бесконечном цикле генерируется сигнал при помощи функций из модуля signal_generator[cite: 27]
        current_time = time.time() - start_time
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude * amplitude
        
        # Напряжение подается на пин OUT блока 12-bit DAC[cite: 27]
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # В блоке finally вызывается «деструктор» объекта класса управления микросхемой MCP4725[cite: 27]
    dac.deinit()