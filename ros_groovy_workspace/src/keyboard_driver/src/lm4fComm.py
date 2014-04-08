#!/usr/bin/env python
import serial

comm = serial.Serial(port='/dev/lm4f', baudrate = 115200);
while true:
	try:
		print comm.read()
		input = raw_input()
		comm.write(input)
	except:
		comm.close()

