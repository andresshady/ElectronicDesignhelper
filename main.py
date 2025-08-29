""" this project is created by Andres Sanchez.
The project consists of electronics support for designing app
"""
#import math

class Circuit:
    def __init__(self,resistance,voltage,current):
        self.resistance = resistance
        self.voltage = voltage
        self.current = current
        self.resistor = {}
        self.capacitor = {}
        self.inductor = {}

    def add_resistor(self,name,value):
        self.resistor[name] = value

    def add_capacitor(self,name,value):
        self.capacitor[name] = value

    def add_inductor(self,name,value):
        self.inductor[name] = value

    def get_resistors(self):
        return self.resistor

    def get_capacitors(self):
        return self.capacitor

    def get_inductors(self):
        return self.inductor

    def calculate_voltage(self):
        return self.current * self.resistance

    def calculate_current(self):
        return self.voltage / self.resistance

    def calculate_power(self):
        return self.voltage * self.current








