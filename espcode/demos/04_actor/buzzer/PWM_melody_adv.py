import machine
import time

buzzer = machine.PWM(machine.Pin(25, machine.Pin.OUT), freq=1, duty_u16=2**16//2)
tonesRaw = {
    'c': 262, # c1
    'cis': 277,
    'des': 277,
    'd': 294,
    'dis': 311,
    'es': 311,
    'e': 330,
    'f': 349,
    'fis': 370,
    'ges': 370,
    'g': 392,
    'gis': 415,
    'as': 415,
    'a': 440, # a1
    'ais': 466,
    'b': 466,
    'h': 494,
}

tones = {}
for i in range(1, 5): # generate more tones
    for t, f in tonesRaw.items():
        tones[t + str(i)] = f * (2**(i-1))
tones[' '] = 0

# add extra tone needed for the melody
tones['h0'] = 247

# melody from Mozart - sonata in e minor - KV304
melody = ['e1', 'g1', 'h1', 'e2', 'g2', 'g2', 'fis2', 'e2', 'dis2', 'e2', 'fis2', 'h1', 'c2', 'h1', 'a1', 'h1', 'c2', 'fis1', 'fis1', 'h1', 'a1', 'g1', 'a1', 'h1', 'h1', 'e1', ' ', 'e1', 'dis1', 'e1', 'fis1', 'dis1', 'h0', ' ', 'fis1', 'e1', 'fis1', 'g1', 'e1', 'h0', ' ', 'g1', 'fis1', 'g1', 'a1', 'fis1', 'g1', 'a1', 'h1', 'g1', 'a1', 'h1', 'c2', 'a1', 'h1']
rhythm = [ 8  ,  8  ,  2  ,  2  ,  2  ,  4   , 8    ,  8  ,  2    ,  4  ,  4    ,  2  ,  8  ,  8  , 2   ,  4  ,  4  ,  2    ,  4    ,  8  ,  8  ,  4  ,  4  ,  4  ,  4  ,  4  ,  8 ,  8  ,  8    ,  8  ,  8    ,  8    ,  4  ,  8 ,  8    ,  8  ,  8    ,  8  ,  8  ,  4  ,  8 ,  8  ,  8    ,  8  ,  8  ,  8    ,  8  ,  8  ,  8  ,  8  ,  8  ,  8  ,  8  ,  8  ,  2  ]

tempo = 2
for tone, length in zip(melody, rhythm):
    frequency = tones[tone]
    print("playing {0} with frequency of {1} Hz and length 1/{2}".format(tone, frequency, length))
    
    if frequency > 0:
        buzzer.init(tones[tone])
        
    time.sleep(tempo/length)
    
    # short pause after tone
    buzzer.deinit()
    time.sleep(0.01)

buzzer.deinit()
