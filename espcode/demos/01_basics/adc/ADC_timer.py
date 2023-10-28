import machine

adc1 = machine.ADC(machine.Pin(32))

def timer_callback_adc(t):
     print(str('%.2f'%((adc1.read()/4095) * 0.95)) + "V")

timer1 = machine.Timer(-1)
timer1.init(period=300, mode=machine.Timer.PERIODIC, callback=timer_callback_adc)

# Achtung: Timer muss deaktiviert werden (Reset oder Ctrl+D soft reboot)