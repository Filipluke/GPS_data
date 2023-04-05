import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

# Wczytanie danych z pliku CSV
with open('Pomiar_1OBD.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')  # separator to średnik
    next(csvreader) # pomiń nagłówek
    czas = []
    predkosc = []
    for row in csvreader:
        czas.append(float(row[0])/1000)
        predkosc.append(float(row[1]))

# Wczytanie danych z pliku Excela
df = pd.read_excel('Pomiary_1GPS.xlsx', usecols=[0,1])
czas_gps =  df.iloc[:,1]
predkosc_gps = df.iloc[:,0].astype(float)  # zmiana typu wartości na float



# Narysowanie wykresów
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Wykres prędkości
ax1.plot(czas, predkosc, label='OBD')
ax1.plot(czas_gps, predkosc_gps, label='GPS')
ax1.set_xlabel('Czas [s]')
ax1.set_ylabel('Predkość Km/h')
ax1.set_title('Wykres predkosci od czasu')
ax1.legend()

plt.show()
