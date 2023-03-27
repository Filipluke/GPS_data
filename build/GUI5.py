import serial
import matplotlib.pyplot as plt
import numpy as np
# ustawienia portu szeregowego
ser = serial.Serial('COM4', 9600)

# przygotowanie wykresu
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 10)  # ustawienie granic osi X
ax.set_ylim(0, 50)
ax.set_xlabel('Czas [s]')  # dodanie jednostek do osi X
ax.set_ylabel('Prędkość')
ax.set_title('Prędkość w czasie rzeczywistym')
xdata, ydata = [], []
text = ax.text(0.05, 0.95, '', transform=ax.transAxes)  # tekst z aktualną wartością
plt.show(block=False)

# odczytywanie prędkości z portu szeregowego i aktualizacja wykresu
while True:
    serial_line = ser.readline().decode().rstrip('\n')
    if serial_line:
        y = float(serial_line)
        x = (len(xdata) + 1) * 0.1  # zmiana wartości na osi X
        xdata.append(x)
        ydata.append(y)
        line.set_data(xdata, ydata)
        text.set_text('Aktualna wartość: {:.2f}'.format(y))  # aktualizacja tekstu z wartością
        ax.relim()
        ax.autoscale_view(True,True,True)
        ax.set_xlim(x-10, x)  # aktualizacja osi X
        fig.canvas.draw()
        fig.canvas.flush_events()