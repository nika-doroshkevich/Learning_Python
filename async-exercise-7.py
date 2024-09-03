import asyncio


# Write a Python program that implements a timeout for an asynchronous
# operation using asyncio.wait_for().


async def time_consuming_task(duration):
    print(f'Starting long operation for {duration} seconds...')
    await asyncio.sleep(duration)
    return f'Long operation completed in {duration} seconds'


async def main():
    timeout = 3
    try:
        result = await asyncio.wait_for(time_consuming_task(8), timeout)
        print(result)
    except asyncio.TimeoutError:
        print(f'Timeout occurred after waiting for {timeout} seconds')


asyncio.run(main())
