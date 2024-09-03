import asyncio


# Write a Python program that creates three asynchronous functions and displays their
# respective names with different delays (1 second, 2 seconds, and 3 seconds).


async def display_name_with_delay(name, delay):
    await asyncio.sleep(delay)
    print(name)


async def main():
    tasks = [
        display_name_with_delay("Async. function-1", 1),
        display_name_with_delay("Async. function-2", 2),
        display_name_with_delay("Async. function-3", 3)
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
