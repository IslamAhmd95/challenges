"""
Problem:
    You have 5 different timers. Each should "sleep" for a different time and print a message once it finishes. Use threads to let them count down simultaneously.
"""


import time
import threading
import concurrent.futures

def con_timer(timer, seconds):
    time.sleep(seconds)

    print(f"Timer {timer} finished after {seconds} seconds")

timers = [5, 3, 1, 4, 2]

start = time.perf_counter()

## without threading
# for index, timer in enumerate(timers):
#     con_timer(index, timer)

## threading (start, join) way
# threads = [threading.Thread(target=con_timer, args=(index, timer)) for index, timer in enumerate(timers)]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()


## using concurrent futures map
# with concurrent.futures.ThreadPoolExecutor() as executer:
#     indices = list(range(len(timers)))
#     executer.map(con_timer, indices, timers)
    
## using concurrent futures submit() + as_completed()
with concurrent.futures.ThreadPoolExecutor() as executer:
    futures = []
    for i, t in enumerate(timers):
        futures.append(executer.submit(con_timer, i, t))

    # This prints results in submission order
    # for f in futures:
    #     f.result()

    # This prints results as each task finishes, not in submission order.
    for f in concurrent.futures.as_completed(futures):
        f.result()


end = time.perf_counter()

print(f"Total time is {end - start:.2f} seconds")


# without threading: 15 seconds
# with threading ways : 5 seconds



"""
Notes:

    | Approach                      | Result Order       | Best For                      |
    | ----------------------------- | ------------------ | ----------------------------- |
    | `executor.map(...)`           | Submission order   | Simplicity, clean syntax      |
    | `submit()` + loop             | Submission order   | More control                  |
    | `submit()` + `as_completed()` | **Finish order** ✅ | Real-time feedback / progress |


    1. map() and submit() both run tasks concurrently using threads (if you're using ThreadPoolExecutor), even if results appear in submission order.

    2. using as_completed with submit is better

"""