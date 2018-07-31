from machine import I2C,Pin,ADC
import utime
list1 = [12,23,13,23,13,5,6,6,7,8,9]
list2 = [23,23,15,78,56]

def i2cinit():
    i2c = I2C(scl=Pin(5),sda=Pin(4),freq=100000)  
    a=i2c.scan()
    if a==0x2c:

    else:

    i2c.readfrom_mem()

def GPIOinit():
	red=Pin(27,Pin.OUT)
	blue=Pin(32,Pin.OUT)
    gree=Pin(33,Pin.OUT)
    btn=Pin(12,Pin.IN,Pin.PULL_UP)
    temp=ADC(0)
    red.value(1)
    blue.value(1)
    green.value(1)

def check(chn):
    mas=i2c.readfrom_mem(0x2c,add[chn],2)
    if mas>=:
    	return()


i2cinit()
GPIOinit()
while(1)
	while(btn.value()==1)
	utime.sleep_ms(1000)
    red.value(1)
    green.value(1)
	for x in range(0,15):
    	stat=check(x)
    	if stat==1:
       		break
    if stat==1：
    	red.value(0)
    else:
    	green.value(0)
    if(temp.read()==0x22):
    	blue.value(1)
    while(btn.value()==1)
    red.value(1)
    green.value(1)
    utime.sleep_ms(1000)

