import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('PomiarySimr/Velocity1.xlsx', usecols=[0,1])
czas_gps =  df.iloc[:,1]
predkosc_gps = df.iloc[:,0].astype(float)  # zmiana typu wartości na float


# Wczytanie danych z pliku Excela
df = pd.read_excel('PomiarySimr/TEST1.xlsx', usecols=[0,1])
czas_quartz =  df.iloc[:,0]
predkosc_quartz = df.iloc[:,1].astype(float)  # zmiana typu wartości na float



# Narysowanie wykresu
plt.plot(czas_quartz, predkosc_quartz, label='Quartz')
plt.plot(czas_gps, predkosc_gps, label='Neo6M')
plt.xlabel('Czas [s]')
plt.ylabel('Predkość Km/h')
plt.title('Wykres predkosci od czasu')
plt.legend()
plt.show()