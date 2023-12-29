import uasyncio as asyncio

async def countdown(name, number, countDown = False):
    for i in range(1, number + 1):
        if countDown:
            print(name, number - i)
        else:
            print(name, i)

        await asyncio.sleep(1)

async def main():
    tasks = [
        asyncio.create_task(countdown("Loop 1", 10)),
        asyncio.create_task(countdown("Loop 2", 5)),
        asyncio.create_task(countdown("Loop 3", 7, True)),
    ]
    
    await asyncio.gather(*tasks)

asyncio.run(main())
