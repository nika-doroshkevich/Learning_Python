import asyncio


# Write a Python program that creates an asyncio event loop and runs a coroutine
# that prints numbers from 1 to 7 with a delay of 1 second each.


async def display_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)


asyncio.run(display_numbers())
