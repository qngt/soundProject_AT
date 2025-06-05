import numpy as np
import sounddevice as sd

fs = 44100  #Abtastrate (Hz)
dauer = 5.0 #(s)
frequenz_a = 100 #(Hz)
frequenz_b = 102 #(Hz)

t = np.linspace(0, dauer, int(fs * dauer), endpoint=False)
#linspace intervall 0 bis 5, anzahl der x-werte die erzeugt werden,(duration)-Wert nicht eingeschlossen
#fs*dauer: abtastwerte insgesamt

ton_a = 0.5 * np.sin(2 * np.pi * frequenz_a * t)
ton_b = 0.5 * np.sin(2 * np.pi * frequenz_b * t)
#Warum 2*pi? -> sin() erwartet einen Winkel in rad.
#Amplitudenarray: ton : 0.5 Faktor für Lautstärkeregelung sonst Übersteuerung
#Amplitude also halbiert
#t wird elementweise eingesetzt also for each

print(f"1. Ton läuft {dauer:.0f} Sekunden lang: ")
sd.play(ton_a, fs)
sd.wait()

print(f"2. Ton läuft {dauer:.0f} Sekunden lang: ")
sd.sleep(1000) #Pause
sd.play(ton_b, fs)
sd.wait()