"""
Problem:
    A thread-safe counter is a counter object that can be safely incremented by multiple threads at the same time without causing data races or incorrect results. It ensures that increments are atomic (only one thread can update it at a time).
"""

import threading
import time
import concurrent.futures


counter = 0
lock = threading.Lock()

def increment(_):
    global counter
    for _ in range(10000):
        with lock:
            counter += 1
        time.sleep(0.0001)  # simulate I/O or time delay

        

start_time = time.perf_counter()

## regular threading way

# threads = [threading.Thread(target=increment, args=[_]) for _ in range(5)]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()


## with concurrent futures submit + as_completed

with concurrent.futures.ThreadPoolExecutor() as executer:
    futures = []
    for _ in range(5):
        futures.append(executer.submit(increment, _))

# for f in futures:
#     f.result()

for f in concurrent.futures.as_completed(futures):
    f.result()



## concurrent futures map way

# with concurrent.futures.ThreadPoolExecutor() as executer:
#     executer.map(increment, range(5))


end_time = time.perf_counter()

print(f"Counter value is {counter} and total time is : {end_time - start_time:.2f}")



# regular way without threading
counter = 0
start_time = time.perf_counter()

for _ in range(5):
    increment(_)

end_time = time.perf_counter()
print(f"Counter value is {counter} and total time is : {end_time - start_time:.2f}")



"""
Notes:
    1. You MUST call .result() or use as_completed() to ensure thread completion.
        - submit() just queues the function.
        - .result() waits for that thread to finish.
        - Otherwise, print might run before threads finish, giving incorrect counter.

    2. Why executor.map() didn’t work as expected?
        - Because executor.map() expects a function and an iterable.
        - It blocks until all threads finish, so no .result() is needed.
        - But in your test, the timing or counter might seem wrong if previous test threads didn’t reset counter = 0.
    
    3. Python GIL = 🔐 one chef in a kitchen → only one thread runs Python bytecode at a time.
"""