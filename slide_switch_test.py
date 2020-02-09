import time
from adafruit_circuitplayground import cp

while True:
    print("Slide switch:", cp.switch)
    ##Printing the status of the slide switch on the board with the switch function of the cp module
    time.sleep(0.1)
    #Pausing for .1 second
