"""โปรแกรมขายรถยนต์"""

n = int(input())

cars = []

for i in range(n):
    _, v = map(int, input().split())
    cars.append(v)

max_v = 0
ans = 0

for i in range(n - 1, -1, -1):
    if cars[i] < max_v:
        ans += 1

    if cars[i] > max_v:
        max_v = cars[i]

print(ans)
