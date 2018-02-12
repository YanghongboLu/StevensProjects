##python code for YL38 and YL69 soil moisture sensor
import RPI.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
channel=11
gpio.setup(channel,gpio.IN)

def callback(channel):
    if gpio.input(channel):
        humidity_controller()#this fun shall controll harware to change soil humidity
        print("soil is dry for plant")
    else:
        print("soil humidity is suitable for plant")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=200)
GPIO.add_event_callback(channel, callback)
 
while True:
  time.sleep(5)
