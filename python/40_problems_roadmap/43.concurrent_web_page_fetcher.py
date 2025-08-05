"""
Problem:    
    You are given a list of fake URLs (e.g., ["page1", "page2", "page3"]). Each URL takes a random amount of time to "respond" (you should simulate that using asyncio.sleep).

    You need to write an asynchronous function that "fetches" each page concurrently and prints when each page is being fetched and when it's done.

    However, to simulate limited system resources (like bandwidth or open connections), you must limit the number of concurrent fetches to only 2 pages at a time using an asyncio.Semaphore.

    At the end, print the total time taken to fetch all pages.
"""

import asyncio
import random
import time


semaphore = asyncio.Semaphore(2)  # max 2 concurrent tasks

async def fetch(page, delay):
    async with semaphore:
        print(f"Fetching data from {page}")
        await asyncio.sleep(delay)
        print(f"Data fetched from {page}")


async def main():
    # pages = ["page1", "page2", "page3"]
    # tasks = [fetch(page, random.randint(1, 4)) for page in pages]
    # await asyncio.gather(*tasks)
    pages = ["page1", "page2", "page3"]
    delays = [random.randint(1, 5) for _ in pages]
    for page, delay in zip(pages, delays):
        print(f"{page} will take {delay} seconds")
    tasks = [fetch(page, delay) for page, delay in zip(pages, delays)]
    await asyncio.gather(*tasks)



start_time = time.perf_counter()
asyncio.run(main())   # what does this line do ?
end_time = time.perf_counter()

print(f"Total time is {end_time - start_time:.2f}")



"""
Notes:
    1. Why async is used
        - async is used before a function definition to make it a coroutine.
        - Coroutine = A special function that can be paused and resumed (like multitasking).
        - Only inside an async def function you can use await.

    2. Why async with is used with Semaphore
        - This means: acquire the semaphore asynchronously.
        - It doesn't block the whole event loop while waiting.
        - Without async, it would be a blocking operation, which goes against the purpose of asyncio.

    3. What does await do?
        - await means: “Pause here, let other tasks run, and come back when this is done.”
        - It’s used with any coroutine or async operation (like await asyncio.sleep(2) or await fetch()).
        - Think of it as:
            "Start this, don’t block me, and come back with the result when it’s ready."

    4. Why use await asyncio.gather(...)
        - gather groups multiple coroutines and runs them concurrently.
        - await is required to wait for all tasks to complete and collect results.

    5. What does asyncio.run(main()) do?
        - It starts the event loop, runs your main() coroutine, and shuts down the loop when done.
        - It’s the entry point of your async program.

    6. Even if you start 3 tasks, only 2 will be inside `async with` at the same time. But the rest aren’t blocked like in threading — they just pause and let the event loop continue running other code.

    7. Synchronous semaphore (e.g. in threads): blocks the thread while waiting.

    8. Asynchronous semaphore (asyncio.Semaphore): waits without blocking, letting the event loop do other work.
"""
