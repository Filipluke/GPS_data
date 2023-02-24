import serial.tools.list_ports

# ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = "COM4"
serialInst.open()

while True:
	if serialInst.in_waiting:
		packet = serialInst.readline()
		print(packet.decode('utf').rstrip('\n'))
