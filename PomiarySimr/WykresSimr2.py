import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Wczytanie danych z pliku Excela
df = pd.read_excel('PomiarySimr/Velocity1.xlsx', usecols=[0,1])
czas_gps =  df.iloc[:,1]
predkosc_gps = df.iloc[:,0].astype(float)  # zmiana typu wartości na float

# Wczytanie danych z pliku Excela
df = pd.read_excel('PomiarySimr/TEST1.xlsx', usecols=[0,1])
czas_quartz =  df.iloc[:,0]
predkosc_quartz = df.iloc[:,1].astype(float)  # zmiana typu wartości na float

# Interpolacja wartości prędkości dla punktów czasowych z tablicy czas_gps
predkosc_quartz_interp = np.interp(czas_gps, czas_quartz, predkosc_quartz)

# Narysowanie wykresu
plt.plot(czas_gps, abs(predkosc_quartz_interp - predkosc_gps), label='Quartz - Neo6M')
plt.xlabel('Czas [s]')
plt.ylabel('Moduł z różnicy prędkości Km/h')
plt.title('Wykres błędu względnego')
plt.legend()
plt.show()

# Wczytanie danych z pliku Excela
df = pd.read_excel('PomiarySimr/Velocity2.xlsx', usecols=[0,1])
czas_gps =  df.iloc[:,1]
predkosc_gps = df.iloc[:,0].astype(float)  # zmiana typu wartości na float

# Wczytanie danych z pliku Excela
df = pd.read_excel('PomiarySimr/TEST2.xlsx', usecols=[0,1])
czas_quartz =  df.iloc[:,0]
predkosc_quartz = df.iloc[:,1].astype(float)  # zmiana typu wartości na float

# Interpolacja wartości prędkości dla punktów czasowych z tablicy czas_gps
predkosc_quartz_interp = np.interp(czas_gps, czas_quartz, predkosc_quartz)

# Narysowanie wykresu
plt.plot(czas_gps, predkosc_quartz_interp - predkosc_gps, label='Quartz - Neo6M')
plt.xlabel('Czas [s]')
plt.ylabel('Moduł z różnicy prędkości Km/h')
plt.title('Wykres błędu względnego')
plt.legend()
plt.show()
