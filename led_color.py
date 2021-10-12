# example code for SGBotic Ultimate SR04 RGB
# This code is to set the RGB inside the transducers 
# to red -> green -> blue, then repeat

from microbit import *

i2cAddr = 0x60
redRegister = 0x02
greeRegister = 0x03
blueRegister = 0x04

light_intensity_full = 0xFF
light_intensity_zero = 0x00

def ledOff():
    i2c.write(i2cAddr, bytes([redRegister,light_intensity_zero]), repeat=False)
    i2c.write(i2cAddr, bytes([greeRegister,light_intensity_zero]), repeat=False)
    i2c.write(i2cAddr, bytes([blueRegister,light_intensity_zero]), repeat=False)
    
while True:
    ledOff()
    #red led on
    i2c.write(i2cAddr, bytes([redRegister,light_intensity_full]), repeat=False)
    sleep(1000)
    
    ledOff()
    # green led on
    i2c.write(i2cAddr, bytes([greeRegister,light_intensity_full]), repeat=False)
    sleep(1000)
    
    ledOff()
    #blue led on
    i2c.write(i2cAddr, bytes([blueRegister,light_intensity_full]), repeat=False)
    sleep(1000)
