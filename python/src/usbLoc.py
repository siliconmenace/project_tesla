#Print info regarding the included locations
import serial

locations=['/dev/usbdev1.8']

for device in locations:
	try:
		ser = serial.Serial( device , 9600)
	except:
		print "Failed to connect on", device

try:
	print ser.readline()
except:
	print "Failed to read!"


