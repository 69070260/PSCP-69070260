"""โปรแกรมกองชาม"""
n = int(input())
count = [0] * 301

for i in range(n):
    x = int(input())
    count[x] += 1

ans = 0
for i in range(1, 301):
    if count[i] > ans:
        ans = count[i]

print(ans)
