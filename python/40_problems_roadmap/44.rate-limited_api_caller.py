"""
Problem:
    You are given a list of URLs. You need to call an asynchronous API (simulated with asyncio.sleep) for each URL, but you can only send N requests at the same time to respect a rate limit. Use asyncio and Semaphore to enforce this limit.
"""

import asyncio
import random
import time


async def delaying():
    delay = random.randint(1, 6)
    await asyncio.sleep(delay)  # simulate network delay
    return delay


# Simulate API call
async def fetch_url(url, semaphore):
    async with semaphore:  # limit concurrent tasks
        print(f"Fetching: {url}")
        delay = await delaying()  # simulate network delay
        print(f"Result for {url} in {delay} seconds")

# Main event runner
async def main(urls, rate_limit):
    semaphore = asyncio.Semaphore(rate_limit)
    tasks = [fetch_url(url, semaphore) for url in urls]
    await asyncio.gather(*tasks)

# Input
urls = [
    "https://example.com/api/1",
    "https://example.com/api/2",
    "https://example.com/api/3",
    "https://example.com/api/4",
    "https://example.com/api/5"
]
rate_limit = 2

# Run
if __name__ == "__main__":

    start_time = time.perf_counter()
    asyncio.run(main(urls, rate_limit))
    end_time = time.perf_counter()
    
    print(f"Total time is {end_time - start_time:.2f}")


