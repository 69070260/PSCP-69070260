"""โปรแกรม SumOfNumber"""

x = int(input())
total = 0

while total != x:
    n = int(input())

    if n == -1:
        break

    total += n

print(total)
