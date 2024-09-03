import asyncio
import random


# Write a Python program to create a coroutine that simulates a time-consuming task
# and use asyncio.CancelledError to handle task cancellation.


async def time_consuming_task():
    print('Time-consuming task started...')
    try:
        for i in range(1, 6):
            await asyncio.sleep(random.randint(1, 5))
            print(f'Step {i} completed')
    except asyncio.CancelledError:
        print('Time consuming task was cancelled')
        raise


async def main():
    task = asyncio.create_task(time_consuming_task())
    await asyncio.sleep(random.randint(1, 3))
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('Main coroutine caught task cancellation!')


asyncio.run(main())
