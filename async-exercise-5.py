import asyncio
import time


# Write a Python program that runs multiple asynchronous tasks concurrently using
# asyncio.gather() and measures the time taken.


async def task1():
    print("Task-1 started")
    await asyncio.sleep(4)
    print("Task-1 completed")


async def task2():
    print("Task-2 started")
    await asyncio.sleep(1)
    print("Task-2 completed")


async def task3():
    print("Task-3 started\n")
    await asyncio.sleep(2)
    print("Task-3 completed")


async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2(), task3())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nAll tasks completed in {:.2f} seconds".format(elapsed_time))


asyncio.run(main())
