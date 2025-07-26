# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 15:29:14 2025

@author: alexo
"""

import sys

if sys.platform == "win32":
    class SMBus:
        def __init__(self, bus):
            print(f"SMBus mock created for bus {bus}")
        def write_byte_data(self, addr, reg, value):
            print(f"Mock: Write to addr {addr:#x}, reg {reg:#x}, value {value:#x}")
        def read_byte_data(self, addr, reg):
            print(f"Mock: Read from addr {addr:#x}, reg {reg:#x}")
            return 0x00
    smbus = sys.modules[__name__]
    smbus.SMBus = SMBus
else:
    import smbus2 as smbus

class I2C_COMMUNICATION(object):
    def __init__(self) -> None:
        self.i2c_address = 0x10
        self.i2c_bus = smbus.SMBus(1)
        
    def generateTelemetry(self, message) -> int:
        self.i2c_bus.write_byte_data(self.i2c_addr, 0x0, message)
        incoming_data = self.i2c_bus.read_byte(self.i2c_addr)
        
        return incoming_data
    
    