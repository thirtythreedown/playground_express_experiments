import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3
i = 0
delay = 1
red = (50,0,0)
##defining some colors
while True:
    if cp.button_a:
        while i < 10:
            cp.pixels[i] = (red)
            time.sleep(delay)
            i += 1
            print(str(i))
        i = 0
        print(str(delay*10)+ " seconds!")
        while i < 10:
            cp.pixels[i] = (0,50,0)
            time.sleep(delay)
            i += 1
            print(str(i))
        i = 0
        print(str(delay*10)+ " seconds!")
        while i < 10:
            cp.pixels[i] = (0,0,50)
            time.sleep(delay)
            i += 1
            print(str(i))
        i = 0
        print(str(delay*10)+ " seconds!")
        while i < 10:
            cp.pixels[i] = (50,50,0)
            time.sleep(delay)
            i += 1
            print(str(i))
        i = 0
        print(str(delay*10)+ " seconds!")
        while i < 10:
            cp.pixels[i] = (0,50,50)
            time.sleep(delay)
            i += 1
            print(str(i))
        i = 0
        print(str(delay*10)+ " seconds!")
        while i < 10:
            cp.pixels[i] = (50,50,50)
            time.sleep(delay)
            i += 1
            print(str(i))
        print(str(delay*10)+ " seconds!")
        cp.pixels.fill((0,0,0))
