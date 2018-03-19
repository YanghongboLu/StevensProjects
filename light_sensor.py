from __future__ import print_function
import time
from upm import pyupm_light as lightObj

def main():
    # Create the light sensor object using AIO pin 0
    sensor = lightObj.Light(0)

    # Read the input and print both the normalized ADC value and a
    # rough lux value, waiting one second between readings
    while 1:
        print(sensor.name() + " normalized value is %f" % sensor.getNormalized()
              + ", which is roughly %d" % sensor.value() + " lux");
        time.sleep(1)

    # Delete the light sensor object
    del lightObj

if __name__ == '__main__':
    main()
