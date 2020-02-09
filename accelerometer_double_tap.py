import time
from adafruit_circuitplayground import cp

cp.detect_taps = 2
##Using the detect_taps function from cp to detect double-taps on accelerometer. Value sets number of taps.

while True:
    if cp.tapped:
    ##If tapping detected
        print("Tapped!")
        ##Giving feedback over console
    time.sleep(0.05)
    ##Pause for 0.05 seconds and not detecting false positives.
