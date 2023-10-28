'''
Verbindungen
Buzzer (KY-006) ... ESP
-                   GND
S                   D25
'''

import machine
import time

buzzer = machine.PWM(machine.Pin(25, machine.Pin.OUT), freq=1, duty_u16=2**16//2)
tones = {
    'c': 262, # c1
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440, # a1
    'h': 494,
    'C': 523, # c2
    ' ': 0,   # pause
}

melody = 'cdefgahC cdefg g aaaag   aaaag   ffffe e ddddc'
tempo = 0.5

for tone in melody:
    frequency = tones[tone]
    print("{0} has a frequency of {1} Hz".format(tone, frequency))
    if frequency > 0:
        buzzer.init(frequency)
        
    time.sleep(tempo)
    
    # short pause after tone
    buzzer.deinit()
    time.sleep(0.01)

buzzer.deinit()
