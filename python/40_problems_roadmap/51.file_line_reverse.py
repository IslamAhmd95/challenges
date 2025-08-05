"""
Problem:
    Create a context manager using @contextlib.contextmanager that opens a file, reverses the lines then writes back, and on exit close the file.
"""

from contextlib import contextmanager


@contextmanager
def handle_file(file_name, mode="r"):
    mode_str = "reading" if mode == "r" else "writing"
    print(f"Opening file {file_name} for {mode_str}")
    file = open(file_name, mode)
    # If an error occurs inside the yield block, the file might not be closed, so better to use try...finally.
    try:
        yield file
    finally:
        print(f"Closing file {file_name}")
        file.close()


with handle_file("sample.txt") as file:
    print("Reading file ... ")
    content = file.readlines()

print("_"*60)

with handle_file("sample.txt", "w") as file:
    print("Writing the reverse content to file ... ")
    for line in reversed(content):
        file.write(line)