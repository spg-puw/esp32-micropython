import uasyncio as asyncio

async def download(duration=8):
    '''simulate a download'''
    print("starting download ...")
    await asyncio.sleep(duration)
    print("download finished ...")

async def count():
    '''do some counting'''
    print("starting count ...")
    i = 0
    while True:
        print(i)
        i += 1
        await asyncio.sleep(1)

async def main():
    try:
        await asyncio.wait_for(download(), timeout=5) # wait to finish for 5 secs
    except asyncio.TimeoutError:
        print("timeout error!")
        
    try:
        await asyncio.wait_for(download(2), timeout=5) # wait to finish for 5 secs
    except asyncio.TimeoutError:
        print("timeout error!")
        
    task = asyncio.create_task(count())
    try:
        await asyncio.wait_for(task, timeout=10) # wait to finish for 10 secs
    except asyncio.TimeoutError:
        task.cancel() # cancel task
        print("task cancelled")

asyncio.run(main())


