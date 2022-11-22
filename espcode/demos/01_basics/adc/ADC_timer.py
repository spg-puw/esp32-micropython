from machine import Pin, ADC, Timer

adc1 = ADC(Pin(32))

def timer_callback_adc(t):
     print(str('%.2f'%((adc1.read()/4095) * 0.95)) + "V")

timer1 = Timer(-1)
timer1.init(period=300, mode=Timer.PERIODIC, callback=timer_callback_adc)

# Achtung: Timer muss deaktiviert werden (Reset oder Ctrl+D soft reboot)