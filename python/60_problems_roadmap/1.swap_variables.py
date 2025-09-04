"""
Problem: 
    Write a Python program that swaps the values of two variables. 
    You should try both the temporary variable method and Python's unpacking method.
"""

# Temporary variable method
def swap_using_temp_var(a, b):
    c = a
    a = b
    b = c
    return a, b

a, b = 5, 10
print("Before swap (temp var):", a, b)
a, b = swap_using_temp_var(a, b)
print("After swap (temp var):", a, b)


print("-" * 40)


# Unpacking method
def swap_using_unpacking(a, b):
    a, b = b, a
    return a, b

a, b = 5, 10
print("Before swap (unpacking):", a, b)
a, b = swap_using_unpacking(a, b)
print("After swap (unpacking):", a, b)
