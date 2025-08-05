"""
Problem:
    Create a decorator factory log_call(times) that:

        Accepts an integer times indicating how many times a function should be executed.

        Returns a decorator that wraps any function and logs:

            The call index (e.g., Call 0#)

            The function name

            The function arguments (both args and kwargs)

            The result of the function

        Each wrapped function should run times times, and all call logs should be returned as a single string, joined by newlines (\n).
"""

def log_call(times):

    def decorator(func):

        def operation(*args, **kwargs):

            # nonlocal times
            # times = 2

            results = []
            for i in range(times):

                result = func(*args, **kwargs)
                results.append(f"Call #{i}, function name is ({getattr(func, "__name__", "unknown name")}), the function arguments are {args, kwargs} and the result is ({result})")

            return "\n".join(results)

        return operation
    
    return decorator


@log_call(3)
def add(a: int, b: int) -> int:
    return a + b

@log_call(1)
def multiply(a: int, b: int) -> int:
    return a * b

@log_call(1)
def introduction(name: str, age: int) -> str:
    return f"My name is {name} and my age is {age}"


print(add(5, 6))
print(multiply(5, 6))
print(introduction(name="Islam", age=30))



    