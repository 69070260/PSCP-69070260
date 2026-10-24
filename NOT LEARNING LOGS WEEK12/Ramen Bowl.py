"""โปรแกรม Ramen"""

n = int(input())
sizes = {}

for _ in range(n):
    size = int(input())

    if size in sizes:
        sizes[size] += 1
    else:
        sizes[size] = 1

piles = 0

for size, count in sizes.items():
    if count > piles:
        piles = count

print(piles)
