# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def ledBlink(x, board_num, interval):
    for i in range(x):
        GPIO.output(board_num, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(board_num, GPIO.LOW)
        time.sleep(interval)
        i+=1

def lightSensor(channel):
    
    for i in range (50):
        light_val = mcp.read_adc(channel)
        print(light_val)

        if (light_val > 100):
            print("bright")
        else:
            print("dark")
        i+=1
        time.sleep(0.1)

# Main program loop.
while True:
    # LED blinks with 500ms intervals
    ledBlink(5, 11, 0.5)

    lightSensor(0)
    

    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)