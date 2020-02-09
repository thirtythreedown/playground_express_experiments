import time
from adafruit_circuitplayground import cp

while True:
##While the board is on...
    cp.red_led = cp.switch
    ##The value of the red LED is tied to the value of the slide switch.
    ##That is actually really elegant.
