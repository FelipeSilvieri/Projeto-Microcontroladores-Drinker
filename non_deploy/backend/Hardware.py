# import RPi.GPIO as gpio
from time import sleep
import time
import paho.mqtt.client as mqtt
import sys
import json
     

def rele_on(rele):
    gpio.output(rele, gpio.LOW)

def rele_off(rele):
    gpio.output(rele, gpio.HIGH)

def rele_off_general(rele1, rele2):
    rele_off(rele1)
    rele_off(rele2)

def make_drink(rele1, rele2, qtd_A, qtd_B):
    rele_on(rele1)
    time.sleep(2*qtd_A)
    rele_off(rele1)
    rele_on(rele2)
    time.sleep(2*qtd_B)
    rele_off(rele2)
    gpio.cleanup()

def on_Message(client, userdata, msg):
    payload =msg.payload.decode("utf-8")
    data = json.loads(payload)

    rele1 = data["rele_pin_a"]
    rele2 = data["rele_pin_b"]
    qtd_A = data["qtd_A"]
    qtd_B = data["qtd_B"]

    make_drink(rele1, rele2, qtd_A, qtd_B)

client = mqtt.Client()
client.on_message = on_Message

if client.connect("broker.hivemq.com",1883,60)!=0:
  print("cannot connect")
  sys.exit(-1)

client.subscribe('microcontroladores/t3',0)

try:
  print("Conectado ao MQTT Broker...")
  client.loop_forever()
except:
  print("Desconectando do MQTT Broker...")

client.disconnect()
