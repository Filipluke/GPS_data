import serial
import time
# Ustawienie parametrów portu szeregowego
ser = serial.Serial()
ser.port = 'COM5'
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE

# Otwarcie portu szeregowego
ser.open()

# Wysłanie wartości HEX

# GGA disable
data = bytearray.fromhex(
    '24 45 49 47 50 51 2c 47 47 41 2a 32 37 0d 0a b5 62 06 01 03 00 f0 00 00 fa 0f')
ser.write(data)
# GLL disable
time.sleep(1)
data = bytearray.fromhex(
    '24 45 49 47 50 51 2c 47 4c 4c 2a 32 31 0d 0a b5 62 06 01 03 00 f0 01 00 fb 11')
ser.write(data)
# VTG disable
time.sleep(1)
data = bytearray.fromhex(
    '24 45 49 47 50 51 2c 56 54 47 2a 32 33 0d 0a b5 62 06 01 03 00 f0 05 00 ff 19')
ser.write(data)
time.sleep(1)

data = bytearray.fromhex(
    '24 45 49 47 50 51 2c 47 53 41 2a 33 33 0d 0a b5 62 06 01 03 00 f0 02 00 fc 13')
ser.write(data)
time.sleep(1)
data = bytearray.fromhex(
    '24 45 49 47 50 51 2c 47 53 56 2a 32 34 0d 0a b5 62 06 01 03 00 f0 03 00 fd 15')
ser.write(data)
time.sleep(1)


# save the changes
data = bytearray.fromhex(
    'B5 62 06 09 0D 00 00 00 00 00 FF FF 00 00 00 00 00 00 17 31 BF')
ser.write(data)

print("zakończono")

# Zamknięcie portu szeregowego
ser.close()
