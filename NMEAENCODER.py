import pynmea2
import serial
import numpy as np


def Start():
    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = ("COM5")
    serialInst.open()

    while True:

        if serialInst.in_waiting:
            packet = serialInst.readline().decode('utf-8')
            if packet.startswith('$GPRMC'):
                msg = pynmea2.parse(packet)
                if msg.spd_over_grnd is not None:
                    print('Prędkość: {:.2f} km/h'.format(msg.spd_over_grnd))


Start()
