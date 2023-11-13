import RPi.GPIO as gpio
from time import sleep
import time


class Hardware():

    def __init__(self, rele1, rele2, adc1, adc2, dose_A, dose_B):
        gpio.setmode(gpio.BCM)
        self.rele1 = rele1
        self.rele2 = rele2
        gpio.setup(rele1, gpio.OUT)
        gpio.setup(rele2, gpio.OUT)
        
        self.adc1 = adc1
        self.adc2 = adc2
        gpio.setup(adc1, gpio.IN)
        gpio.setup(adc2, gpio.IN)
        
        self.qtd_A = dose_A
        self.qtd_B = dose_B

        self.rele_off_general()
        

    def rele_on(self, rele):
        #rele.off()
        gpio.output(rele, gpio.LOW)

    def rele_off(self, rele):
        #rele.on()
        gpio.output(rele, gpio.HIGH)

    def rele_off_general(self):
        self.rele_off(self.rele1)
        self.rele_off(self.rele2)

    def conversion_factor(self, value):
        return round((65535/(value) * 100) - 100)

    def activate_bomb(self, rele):
        self.rele_on(rele)

    def deactivate_bomb(self, rele_number, adc):
        start_time = time.time()
        actual_time = time.time()
        moisture = gpio.input(adc)

        while ((self.conversion_factor(moisture) >= 45) and (time.time() - start_time < 5)):
            moisture = gpio.input(adc)
            actual_time = time.time()

        self.rele_off(rele_number)

        if (time.time() - start_time < 5):
            return False

        return True

    def make_drink(self):
        #self.activate_bomb(self.rele1)
        #self.activate_bomb(self.rele2)
        self.rele_on(self.rele1)
        time.sleep(2*self.qtd_A)
        self.rele_off(self.rele1)
        self.rele_on(self.rele2)
        time.sleep(2*self.qtd_B)
        self.rele_off(self.rele2)
        #self.deactivate_bomb(self.rele1, self.adc1)
        #self.deactivate_bomb(self.rele2, self.adc2)
        #if self.deactivate_bomb(self.rele1, self.adc1):
        #    sleep(0.5)
        #     self.activate_bomb(self.rele2)
        #    self.deactivate_bomb(self.rele2, self.adc2)
        gpio.cleanup()
