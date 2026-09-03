"""ผลรวมของค่าที่มากกว่า"""
n = int(input())

total = 0
values = []

for _ in range(n):
    a = int(input())
    b = int(input())

    if a > b:
        bigger = a
    else:
        bigger = b

    values.append(bigger)
    total += bigger

if n == 1:
    print(values[0])
else:
    print(" + ".join(map(str, values)), "=", total)
