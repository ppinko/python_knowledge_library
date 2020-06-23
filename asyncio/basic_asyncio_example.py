import asyncio
import sys
import os

async def myCorutine():
    while True:
        await asyncio.sleep(1)
        print("My Coroutine")

async def secondCoroutine():
    while True:
        await asyncio.sleep(1)
        print("Second Coroutine")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(myCorutine())
    asyncio.ensure_future(secondCoroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
