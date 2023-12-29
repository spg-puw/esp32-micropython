import uasyncio as asyncio

async def calcDivide(a, b):
    print("do calculation: dividing {a} by {b}".format(a=a, b=b))
    await asyncio.sleep(5)
    if b == 0:
        raise ZeroDivisionError("divide by zero error")
    return a / b

async def main():
    result = await asyncio.gather(
        calcDivide(100, 1),
        calcDivide(100, 0),
        calcDivide(100, 5),
        return_exceptions=True,
    )

    print("\ntakes some time ...\n\nresults:")
    for r in result:
        if isinstance(r, Exception):
            print("Exception ({}): {}".format(type(r).__name__, r))
        else:
            print("Result: {}".format(r))

asyncio.run(main())
