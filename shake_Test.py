from adafruit_circuitplayground import cp
print("GEtting started with the shake program")
while True:
    if cp.shake():
        ##If board is shaked
        print("Shake detected")
        ##Printing out feedback
