import time
from adafruit_circuitplayground import cp

cp.detect_taps = 1
##Using the detect_taps function from cp to detect double-taps on accelerometer. Value sets number of taps.
cp_count = 0

while cp_count < 2:
    if cp.tapped:
    ##If tapping detected
        print("Tapped!")
        ##Giving feedback over console
        cp_count = cp_count+1
        ##Giving visual feedback with onboard LED using red_led function from cp library
        time.sleep(0.1)
        ##Pause for 0.1 seconds and not detecting false positives.
print("That's two single taps! You unlocked double taps.")
cp.detect_taps = 2
cp_count = 0

while cp_count < 2:
    if cp.tapped:
        print("Tapped!")
        cp_count = cp_count+1
        time.sleep(0.1)
print("That's two double taps! You completed the combo.")

while True:
    cp.red_led = True
