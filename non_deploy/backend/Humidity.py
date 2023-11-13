import RPi.GPIO as gpio
import time


class Humidity():
    
    def __init__(self):
        gpio.setmode(gpio.BCM)
        
    def read_humidity(self, adc):
        gpio.setup(adc, gpio.IN)
        moisure = gpio.input(adc)
        return self.conversion_factor(moisture)

    def conversion_factor(self, value):
        return round((65535/(value) * 100) - 100)
