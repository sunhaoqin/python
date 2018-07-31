import serial
import serial.tools.list_ports

ser = serial.Serial(
  port='COM22',
  baudrate=9600
)
data = ''


while 1:
    data = ser.read(1)
    print (data)