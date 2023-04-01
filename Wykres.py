import matplotlib.pyplot as plt
import csv
import pandas as pd

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

# Narysowanie wykresu
plt.plot(czas, predkosc, label='OBD')
plt.plot(czas_gps, predkosc_gps, label='GPS')
plt.xlabel('Czas [s]')
plt.ylabel('Predkość Km/h')
plt.title('Wykres predkosci od czasu')
plt.legend()
plt.show()