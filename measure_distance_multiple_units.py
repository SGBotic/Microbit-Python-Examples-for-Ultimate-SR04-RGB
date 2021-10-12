# example code for SGBotic Ultimate SR04 RGB
# this code is to use three sensor to measure 
# distance of the obstacles

from microbit import *

#define I2C address of the sensors
i2cAddr1 = 0x59
i2cAddr2 = 0x60
i2cAddr3 = 0x61

triggerRegister = 0x01
triggerCmd = 0x01
result_cm_register = 0x0A

#convert byte array to integer
def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
    
data = bytes([2])
while True:
    #trigger sensor 1 to 3
    i2c.write(i2cAddr1, bytes([triggerRegister, triggerCmd]), repeat=False)
    i2c.write(i2cAddr2, bytes([triggerRegister, triggerCmd]), repeat=False)
    i2c.write(i2cAddr3, bytes([triggerRegister, triggerCmd]), repeat=False)
    # wait for sound wave to return
    sleep(50)
    
    #read back measured distance of sensor 1
    i2c.write(i2cAddr1, bytes([result_cm_register]), repeat=False)
    data = i2c.read(i2cAddr1, 2)
    #Convert returned data to integer
    dist1 = bytes_to_int(data)
    
    #read back measured distance of sensor 2
    i2c.write(i2cAddr2, bytes([result_cm_register]), repeat=False)
    data = i2c.read(i2cAddr2, 2)
    dist2 = bytes_to_int(data)
    
    #read back measured distance of sensor 3
    i2c.write(i2cAddr3, bytes([result_cm_register]), repeat=False)
    data = i2c.read(i2cAddr3, 2)
    dist3 = bytes_to_int(data)
    
    #print to serial
    print("cm #1: %s  cm #2: %s  cm #3: %s" % (dist1,  dist2,  dist3))
    sleep(100)
