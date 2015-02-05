#!/usr/bin/python

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)

ser = serial.Serial('/dev/ttyUSB0', 9600)

print '\r\nEnter your commands below.\r\nInsert "exit" to leave the application.'
print '\r\n(Enter "10" for device help)\r\n'

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(input + '\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print ">>" + out
