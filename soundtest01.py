import numpy as np
import sounddevice as sd

fs = 44100  # Abtastrate (Hz) -> Abtasttheorem
dauer = 5.0 # Sekunden
frequenz_a = 200
frequenz_b = 210

t = np.linspace(0, dauer, int(fs * dauer), endpoint=False)
#linspace intervall 0 bis 5, anzahl der x-werte die erzeugt werden,(duration)-Wert nicht eingeschlossen
#fs*dauer: abtastwerte insgesamt

ton_a = 0.5 * np.sin(2 * np.pi * frequenz_a * t)
ton_b = 0.5 * np.sin(2 * np.pi * frequenz_b * t)
#Amplitudenarray: ton : 0.5 Faktor für Lautstärkeregelung sonst Übersteuerung
#Amplitude also halbiert
#t wird elementweise eingesetzt also for each




sd.play(ton_a, fs)
sd.wait()  #Warten, bis Ton fertig ist
sd.play(ton_b, fs)

#Wie möchte ich mehrere Töne hintereinander abspielen lassen? eig ganz gut manuell weil ich nur frquency var
#umschreiben muss. Werte