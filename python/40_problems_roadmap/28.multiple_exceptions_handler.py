"""
Problem:
    Write a function that performs a set of operations — such as division, type casting, or file access — and gracefully handles multiple exception types using try-except. Your function should log or return custom error messages based on the exception caught.
"""
import os


# print(10/0)   # here i can know the exception name from the output on the terminal

def process_data(num_str, nums, file_name):

    result = dict()

    try:
        a = int(nums['a'])
        b = int(nums['b'])
        result['sum'] = a + b
        result['division'] = a / b
    except KeyError:
        result['math_error'] = "'a' and 'b' keys must be present in the 'nums' dictionary."
    except TypeError:
        result['math_error'] = "'a' and 'b' must be numbers."
    except ValueError:
        result['math_error'] = "'a' and 'b' must be integers or convertible to integers."
    except ZeroDivisionError:
        result['division_error'] = "Cannot divide by zero."
    finally:
        result['math_message'] = "Math operations handled."


    try:
        result['conversion'] = int(num_str)
    except ValueError:
        result['conversion_error'] = "Provided input could not be converted to an integer."
    finally:
        result['conversion_message'] = "Conversion operation handled."


    try:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        with open(path) as f:
            result['file_content'] = f.read()
    except FileNotFoundError:
        result['file_error'] = f"File '{file_name}' not found."
    finally:
        result['file_message'] = "File handling completed."


    return result


print(process_data("10", {'a': 5, 'b': 0}, "missing.txt"))
print(process_data("10", {'a': 'hello', 'b': 4}, "missing.txt"))
print(process_data("h", {'a': 5}, "sample.txt"))




"""
Notes:
    - ValueError: Raised when a valid type receives a bad value.
        - int("abc")  # ValueError - 'abc' is not a valid int
    - TypeError: Raised when the operation is invalid for the type.
        - "5" + 3        # TypeError - can't add str and int
        - None / 2       # TypeError - unsupported operand type(s)


"""