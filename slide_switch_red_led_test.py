import time
from adafruit_circuitplayground import cp

while True:
##While the board is on...
    if cp.switch:
    ##If the slide switch is in the ON/True position...
        cp.red_led = True
        ##...Turning on onboard red LED
    else:
    ##Any other scenario (slide switch in OFF/False position, malfunctioning)...
        cp.red_led = False
        ##...Turning off the onboard red LED
