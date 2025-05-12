import numpy as np
import sounddevice as sd


fs = 44100  # Abtastrate (Hz) -> Abtasttheorem
duration = 5.0  # Dauer in Sekunden
frequency = 100  # Frequenz in Hz

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
#linspace intervall 0 bis 5, anzahl der x-werte die erzeugt werden,(duration)-Wert nicht eingeschlossen

tone = 0.5 * np.sin(2 * np.pi * frequency * t)
#ZeitArray: tone : 0.5 Faktor für Lautstärkeregelung sonst Übersteuerung
#

sd.play(tone, samplerate=fs)
sd.wait()  #Warten, bis Ton fertig ist

#Wie möchte ich mehrere Töne hintereinander abspielen lassen? eig ganz gut manuell weil ich nur frquency var
#umschreiben muss. Werte