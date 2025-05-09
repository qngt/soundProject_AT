import numpy as np
import sounddevice as sd

fs = 44100  # Abtastrate (Hz)
duration = 5.0  # Dauer in Sekunden
frequency = 100  # Frequenz in Hz

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    #linspace intervall 0 bis 5, anzahl der werte die erzeugt werden, Endwert (5.0) nicht eingeschlossen
tone = 0.5 * np.sin(2 * np.pi * frequency * t) #ZeitArray: tone

sd.play(tone, samplerate=fs)
sd.wait()  # Warten, bis Ton fertig ist

