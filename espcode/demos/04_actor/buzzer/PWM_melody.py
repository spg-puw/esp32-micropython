from machine import Pin, PWM
from time import sleep
buzzer = PWM(Pin(25, Pin.OUT), freq=440, duty=512)
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    ' ': 0,
}
melody = 'cdefg g aaaag aaaag ffffee ddddc'
rhythm = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
tempo = 5
for tone, length in zip(melody, rhythm):
    print(tone)
    buzzer.freq(tones[tone])
    sleep(tempo/length)

buzzer.deinit()