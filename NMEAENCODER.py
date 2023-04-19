import pynmea2
import serial
import numpy as np

ser = serial.Serial('COM4', 9600)


def Start():
    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = ("COM4")
    serialInst.open()

    while True:

        if serialInst.in_waiting:
            packet = serialInst.readline()
            if packet.startswith('$GPRMC'):
                msg = pynmea2.parse(line)
                if msg.spd_over_grnd is not None:
                    print('Prędkość: {:.2f} km/h'.format(msg.spd_over_grnd))


# Otwórz plik z danymi GPS
with open('dane_gps.txt', 'r') as f:
    for line in f:
        # Sprawdź, czy linia zaczyna się od $GPRMC (to linia z informacją o prędkości)
        if line.startswith('$GPRMC'):
            # Parsuj dane z linii
            msg = pynmea2.parse(line)
            # Sprawdź, czy prędkość jest dostępna w danych GPS
            if msg.spd_over_grnd is not None:
                # Wyświetl prędkość w km/h
                print(
                    'Prędkość: {:.2f} km/h'.format(msg.spd_over_grnd * 1.852))
