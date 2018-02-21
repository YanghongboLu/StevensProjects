from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_mg811 as sensorObj

def main():
    # Instantiate an MG811 on analog pin A0, and digital pin D2 with an
    # analog reference voltage of MG811_AREF (5.0)

    sensor = sensorObj.MG811(0, 2, 5.0)

    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    # Every tenth of a second, sample the sensor and output it's
    # detected CO2 concentration in parts per million (ppm)

    while (1):
        print("CO2 concentration in PPM: ", sensor.ppm())
        time.sleep(.1)

if __name__ == '__main__':
    main()
