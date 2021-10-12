# example code for SGBotic Ultimate SR04 RGB
# this code is to change the I2C address of the above mentioned module
# Power cycle the unit for this change to take effect

from microbit import *

#define I2C address
i2cAddr = 0x60
setI2cAddressRegister = 0xE0

#valid value from 0x08 to 0x71
newI2cAddr = 0x61

#start of main program
i2c.write(i2cAddr, bytes([setI2cAddressRegister, newI2cAddr]), repeat=False)
print("I2C address has been changed to %s" % newI2cAddr)
print("Power cycle the unit for this change to take effect")
print("")
  
