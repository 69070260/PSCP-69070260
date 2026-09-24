"""ทำ Arrow"""
x = input()
n = int(input())

for direction in x:

    if direction == "R":
        for i in range(n):
            print("  " * i + "*" * (n - i))

        for i in range(n - 2, -1, -1):
            print("  " * i + "*" * (n - i))

    elif direction == "L":
        for i in range(n):
            print(" " * (n - i - 1) + "*" * (n - i))

        for i in range(n - 2, -1, -1):
            print(" " * (n - i - 1) + "*" * (n - i))

    print()
