## DHT11 gets temperature and humidity data from Raspberry Pi
import RPI.GPIO as gpio
import time

port=13 #set pin13 as input pin

gpio.setwarning(False)
gpio.setmode(gpio.BOARD)
time.sleep(1)
data=[]

def delay(i):# set delay
    a=0
    for j in range(i):
        a+1
j=0
i=1
#enabel port
gpio.setup(port,gpio.OUT)
gpio.output(port,gpio.LOW)
gpio.sleep(0.02)
gpio.output(port,gpio.HIGH)

#wait to response
gpio.setup(port,gpio.IN)

while gpio.input(port)==1:
    continue

while gpio.input(port)==0:
    continue

while gpio.input(port)==1:
    continue

#get data
while j<40:
    k=0
    while gpio.input(port)=0:
        continue

    while gpio.input(port)==1:
        k+=1
        if k>100:break
    if k<3:
        data.append(0)
    else:
        data.paaend(1)
    j+=1

#get temperature

humidity_bit=data[0:8]  
humidity_point_bit=data[8:16]  
temperature_bit=data[16:24]  
temperature_point_bit=data[24:32]  
check_bit=data[32:40]  
  
humidity=0  
humidity_point=0  
temperature=0  
temperature_point=0  
check=0

#transfer data into decimal 
for i in range(8):
    humidity+=humidity_bit[i]*2**(7-i)  
    humidity_point+=humidity_point_bit[i]*2**(7-i)  
    temperature+=temperature_bit[i]*2**(7-i)  
    temperature_point+=temperature_point_bit[i]*2**(7-i)  
    check+=check_bit[i]*2**(7-i)

tmp=humidity+humidity_point+temperature+temperature_point

if check==tmp:  
    print "temperature is ", temperature,"humidity is ",humidity,"%" 
