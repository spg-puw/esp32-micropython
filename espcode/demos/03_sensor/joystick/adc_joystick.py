import machine
import time

#GPIOs für ADC: 32, 33, 34, 35, 36 und 39

joyX = machine.Pin(34, machine.Pin.IN)
joyY = machine.Pin(35, machine.Pin.IN)

joyXadc = machine.ADC(joyX)
joyXadc.atten(machine.ADC.ATTN_11DB) #Lesebereich 0,15 bis 2,5 V
joyYadc = machine.ADC(joyY)
joyYadc.atten(machine.ADC.ATTN_11DB) #Lesebereich 0,15 bis 2,5 V

while True:
    valX = joyXadc.read()  #unsigned integer mit range 0-4095
    valY = joyYadc.read()  #unsigned integer mit range 0-4095
    print("X Wert: {x}      Y-Wert: {y}".format(x=valX, y=valY))
    time.sleep(0.5) #0.5 sekunden
    
