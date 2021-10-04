##################################################################################
# laika_gas_sensors.py - reads MQ series gas sensors and prints out their data
# values. Based on the Adafruit ads1x15_ex_singleended.py example script, so credit
# for the code goes to Adafruit.
#
# Philip R. Moyer
# March 2016
##################################################################################

#########################
# Imports
#########################

import time, signal, sys
from adafruit_ads1x15 import ads1115


#########################
# Globals
#########################

voltVector = [] # Vector of read voltages

#########################
# Classes and Methods
#########################


#########################
# Functions
#########################

def signal_handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C to exit'

#########################
# Main
#########################

ADS1015 = 0x00 # 12-bit ADC
ADS1115 = 0x01 # 16-bit ADC

# Select the gain
# gain = 6144 # +/- 6.144V
gain = 4096 # +/- 4.096V
# gain = 2048 # +/- 2.048V
# gain = 1024 # +/- 1.024V
# gain = 512 # +/- 0.512V
# gain = 256 # +/- 0.256V

# Select the sample rate
# sps = 8 # 8 samples per second
# sps = 16 # 16 samples per second
# sps = 32 # 32 samples per second
# sps = 64 # 64 samples per second
# sps = 128 # 128 samples per second
sps = 250 # 250 samples per second
# sps = 475 # 475 samples per second
# sps = 860 # 860 samples per second

# Initialise the ADCs using the default mode (use appropriate I2C address)
adc = ADS1x15(ic=ADS1115)
adc2 = ADS1x15(ic=ADS1115, address=0x49)
adc3 = ADS1x15(ic=ADS1115, address=0x4a)

while (True):
    voltVector = []
    # MQ-2
    volts = adc.readADCSingleEnded(0, gain, sps) / 1000
    # print "MQ-2 %.6fv" % (volts)
    voltVector.append(volts)

    
    print(voltVector)

