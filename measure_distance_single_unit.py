# example code for SGBotic Ultimate SR04 RGB
# this code is to measure distance of an obstacle

from microbit import *

i2cAddr = 0x60
triggerRegister = 0x01
triggerCmd = 0x01
result_cm_register = 0x0A

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
    
data = bytes([2])
while True:
    #trigger
    i2c.write(i2cAddr, bytes([triggerRegister, triggerCmd]), repeat=False)
    sleep(50)
    
    #read back measured distance
    i2c.write(i2cAddr, bytes([result_cm_register]), repeat=False)
    data = i2c.read(i2cAddr, 2)
    dist = bytes_to_int(data)
    
    print("distance in cm: %s" % dist)
    sleep(100)
