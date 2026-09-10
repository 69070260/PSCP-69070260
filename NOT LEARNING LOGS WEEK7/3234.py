"""ไฟคริสตมาส"""

start, n = input().split()
n = int(n)

if start == "R":
    start = 0
elif start == "G":
    start = 1
else:
    start = 2

colors = ["Red", "Green", "Blue"]

for i in range(n):
    print(colors[(start + i) % 3], end=" ")
