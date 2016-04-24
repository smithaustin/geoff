import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

def callProtocol(number):
    writeNumber(number)
    print("Initianting protocol " + str(number))
    time.sleep(1)
    return(readNumber())

#This is the function to be called
def retrieve(type):

    if(type == "ph"):
        iterations = callProtocol(1)
        remainder = callProtocol(2)
        return(iterations*256+remainder)

    if(type == "temperature"):
        return(callProtocol(3))