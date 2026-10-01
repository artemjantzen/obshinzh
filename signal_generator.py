import numpy as np #[cite: 22]
import time #[cite: 22]

def get_sin_wave_amplitude(freq, current_time):
    # Принимает на вход частоту синусоидального сигнала и момент времени[cite: 22]
    # Возвращает сдвинутую вверх и нормализованную форму функции sin(2*pi*f*t)[cite: 22]
    # Значение от -1 до 1 сдвигается вверх и становится от 0 до 2, а затем приводится к диапазону от 0 до 1[cite: 22]
    return (np.sin(2 * np.pi * freq * current_time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    # Принимает на вход частоту дискретизации и ждёт в течение одного периода дискретизации
    period = 1.0 / sampling_frequency
    time.sleep(period)