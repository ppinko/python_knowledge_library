import asyncio
import sys
import os
from aioconsole import ainput

async def myCorutine():
    while True:
        await asyncio.sleep(1)
        print("My Coroutine")

async def secondCoroutine():
    while True:
        await asyncio.sleep(1)
        x = input("Enter an int: ")
        print(x)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(myCorutine(), secondCoroutine())
    loop.run_forever()
except KeyboardInterrupt:
    asyncio.ensure_future()
    pass
finally:
    print("Closing Loop")
    loop.close()

"""
async def main():
    menu()
    while True:
        cmd = await ainput('Insert Command >')
        cmd_cls = CommandFactory.get_cmd(cmd)
        if not cmd_cls:
            print('Unknown: {}'.format(cmd))
        elif cmd_cls.asyn:
            await cmd_cls(client).run()
        else:
            cmd_cls(client).run()
"""
