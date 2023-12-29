import uasyncio as asyncio

async def say(s, delay = 1):
    await asyncio.sleep(delay)
    print(s)

async def main():
    await asyncio.gather(
        say("Hello", 1),
        say("World", 2),
        say("!", 3),
    )

asyncio.run(main())
