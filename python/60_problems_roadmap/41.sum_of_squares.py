"""
Problem:
    You're given a list of integers. Your task is to compute the sum of squares of these numbers. This is a CPU-bound task, so use Python multiprocessing to speed it up.
"""

import multiprocessing
import concurrent.futures
import time

## first way

# def square(n):
#     time.sleep(1)
#     return n * n

# start_time = time.perf_counter()


# with multiprocessing.Pool() as pool:
#     results = pool.map(square, range(1, 6))

# total = 0
# total = sum(results)

# end_time = time.perf_counter()



## second way

# def square(q, n):
#     time.sleep(1)
#     q.put(n * n)

# start_time = time.perf_counter()

# q = multiprocessing.Queue()

# processes = []
# for i in range(1, 6):
#     process = multiprocessing.Process(target=square, args=[q, i])
#     process.start()
#     processes.append(process)

# for p in processes:
#     p.join()
    
# total = 0    
# for _ in range(len(processes)):
#     total += q.get()

# end_time = time.perf_counter()

# print(f"Total: {total}, Time: {end_time - start_time:.2f} seconds")


## third way

def square(n):
    time.sleep(1)
    return n * n

start_time = time.perf_counter()


with concurrent.futures.ProcessPoolExecutor() as pool:
    futures = [pool.submit(square, i) for i in range(1, 6)]

total = 0
for r in concurrent.futures.as_completed(futures):
    total += r.result()


end_time = time.perf_counter()

print(f"Total: {total}, Time: {end_time - start_time:.2f} seconds")


"""
Notes:
    1. Use `multiprocessing.Queue()` to share data between processes.
    2. Each process puts its result into the shared queue.
    3. Collect all results using `q.get()` once per process.
    4. Important: `multiprocessing.Queue` is a class — must instantiate it with `()`.
    5. 
    | Method                         | Time    | Notes                              |
    | ------------------------------ | ------- | ---------------------------------- |
    | `multiprocessing.Pool.map()`   | \~1.02s | Best for simple parallel tasks.    |
    | Manual `Process` + `Queue`     | \~1.02s | More control; same performance.    |
    | `ProcessPoolExecutor + submit` | \~2.02s | Works, but slower due to overhead. |



"""