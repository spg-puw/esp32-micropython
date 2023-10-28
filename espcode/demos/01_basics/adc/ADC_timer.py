import machine

adc1 = machine.ADC(machine.Pin(32))

def timerCallback(t):
    print("Wert 12bit: {0}   Wert 16bit: {1}   Spannung: {2} V".format(adc1.read(), adc1.read_u16(), adc1.read_uv()/1000000))

timer1 = machine.Timer(-1)
timer1.init(period=300, mode=machine.Timer.PERIODIC, callback=timerCallback)

# Achtung: Timer muss deaktiviert werden (Reset oder Ctrl+D soft reboot)