from adafruit_circuitplayground import cp

while True:
    if cp.shake(shake_threshold=20):
        print("Shake detected!")
        cp.red_led = True
    else:
        cp.red_led = False
