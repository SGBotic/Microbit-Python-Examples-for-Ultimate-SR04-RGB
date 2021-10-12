# example code for SGBotic Ultimate SR04 RGB
# this code is to read the firmware version

from microbit import *

i2cAddr = 0x60
versionRegister = 0xF0

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

    
version = bytearray([1])

#start of main program
i2c.write(i2cAddr, bytes([versionRegister]), repeat=False)
version = i2c.read(i2cAddr, 1)
print("firmware version: %s" % bytes_to_int(version))
print("")
print("")
  
