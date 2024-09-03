import asyncio


# Write a Python program that creates an asynchronous function
# to print "Python Exercises!" with two seconds delay.


async def print_delayed_message():
    await asyncio.sleep(2)
    print("Python Exercises!")


async def main():
    await print_delayed_message()


asyncio.run(main())
