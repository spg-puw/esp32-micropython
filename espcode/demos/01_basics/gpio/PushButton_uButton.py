from ubutton import uButton
import uasyncio as asyncio
import machine

def main():
    button = uButton(
        machine.Pin(0, machine.Pin.IN),
        cb_short = lambda: print('short press'),
        short_wait=True,
        cb_long = lambda: print('long press'),
        bounce_time=25,
        long_time=500,
        act_low=True
    )

    loop = asyncio.get_event_loop()
    loop.create_task(button.run())
    loop.run_forever()

if __name__ == '__main__':
    main()
