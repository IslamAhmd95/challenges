"""
Problem:
    You’re given a list of time-consuming tasks, each represented by a number. Each task takes n seconds to complete, where n is the number itself. Your goal is to simulate parallel execution using multiple workers (or threadors), and compute the total time required to finish all tasks if they are run in parallel using k workers.
"""

import threading
import time


def workers(semaphore, *data):
    index, task = data
    with semaphore:
        print(f"Task number {index} has been started")
        time.sleep(task)
        print(f"Task number {index} has been finished")


tasks = [4, 2, 8, 3, 1]
k = 2
semaphore = threading.Semaphore(k)

start_time = time.perf_counter()

threads = []
for index, task in enumerate(tasks):
    thread = threading.Thread(target=workers, args=[semaphore, index, task])
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()


end_time = time.perf_counter()

print(f"Total time is {end_time - start_time:.2f}")
