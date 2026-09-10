"""กระต่ายอ้วน"""

n = int(input())

count = 0
max_weight = 0
max_name = ""

for _ in range(n):
    name, weight = input().split()
    weight = int(weight)

    if weight > 15:
        count += 1

    if weight > max_weight:
        max_weight = weight
        max_name = name

print(count)
print(max_name)
