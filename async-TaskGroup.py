import asyncio


async def worker(n):
    await asyncio.sleep(n)
    if n == 2:
        raise ValueError(f"Worker {n} failed!")
    print(f"Worker {n} finished")


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(worker(1))
            tg.create_task(worker(2))
            tg.create_task(worker(3))
    except* Exception as e:
        print(f"Error occurred: {e}")


asyncio.run(main())
