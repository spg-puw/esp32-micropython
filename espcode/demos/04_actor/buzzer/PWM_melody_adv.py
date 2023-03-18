from machine import Pin, PWM
from time import sleep
buzzer = PWM(Pin(25, Pin.OUT), freq=0, duty=512)
tonesRaw = {
    'c': 262,
    'cis': 277,
    'd': 294,
    'dis': 311,
    'e': 330,
    'f': 349,
    'fis': 370,
    'g': 392,
    'gis': 415,
    'a': 440,
    'ais': 466,
    'b': 494,
}
tones = {}
for i in range(1, 5):
    for t, f in tonesRaw.items():
        tones[t + str(i + 3)] = f * (2**(i-1))
tones[' '] = 0

melody = ['c4', 'cis4', 'd4', 'dis4', 'e4']
rhythm = [8, 8, 8, 8, 8]

tempo = 5
for tone, length in zip(melody, rhythm):
    print("playing", tone, "freq", tones[tone], "len", length)
    buzzer.freq(tones[tone])
    sleep(tempo/length)

buzzer.deinit()