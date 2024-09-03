import asyncio
import random


# Write a Python program that uses asyncio queues to simulate a producer-consumer
# scenario with multiple producers and a single consumer.


async def producer(queue, id):
    for i in range(3):
        item = f"Item: {id}-{i}"
        await queue.put(item)
        print(f"Producer {id} produced-> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer consumed {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)
    await consumer_task


asyncio.run(main())
