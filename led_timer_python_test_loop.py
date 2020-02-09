import time
from adafruit_circuitplayground import cp

i = 0
counter = 0
##Initializing pixel i value and counter value
delay = 0.1
##Defining delay

red = (50,0,0)
yellow = (50,50,0)
green = (0,50,0)
blue = (0,50,50)
purple = (50,0,50)
white = (50,50,50)
off = (0,0,0)
##Defining colors
colors_list = [red, yellow, green, blue, purple, white]
##Storing colors into a list to pick from

def pixels_blink():
    """blinking method to signal end of timer loop"""
    cp.pixels.fill(red)
    time.sleep(0.5)
    cp.pixels.fill(off)
    time.sleep(0.5)
    cp.pixels.fill(red)
    time.sleep(0.5)

while True:
    if cp.button_a:
        while counter < 6:
            while i < 10:
                cp.pixels[i] = (colors_list[counter])
                time.sleep(delay)
                i += 1
                print(str(i))
            if i == 10:
            ##I feel like I'm getting something wrong here.
                counter += 1
                i = 0
                print("Current counter value: " + str(counter))
        print("Done counting! Final counter value: " + str(counter))
        pixels_blink()
        cp.pixels.fill(off)
        counter = 0
        i = 0
