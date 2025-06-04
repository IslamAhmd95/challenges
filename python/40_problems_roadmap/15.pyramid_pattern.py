"""
Problem:
    Print a pyramid pattern of asterisks (*) using nested loops. The number of rows in the pyramid is based on user input.
"""

while True:

    n = input("Enter the number of rows in the pyramid or (type q to quit): ").strip()
    if n.lower() == 'q':
        print("Game done\n")
        break

    try:
        n = int(n)
        width = 2 * n
        for i in range(1, width, 2):
            stars = i * "*"
            print(stars.center(width - 1))

    except ValueError as e:
        print("Value must be an integer\n")
        continue