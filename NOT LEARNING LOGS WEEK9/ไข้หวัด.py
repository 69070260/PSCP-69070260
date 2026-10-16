"""โปรแกรม ไข้หวัดกระต่าย"""
r, c = map(int, input().split())
x, y = map(int, input().split())
n = int(input())

city = [[0] * c for i in range(r)]

for i in range(n):
    a, b = map(int, input().split())

    for j in range(r):
        for k in range(c):
            d = max(abs(j - a), abs(k - b))

            if not d:
                city[j][k] = 100
            elif d == 1 and city[j][k] < 60:
                city[j][k] = 60
            elif d == 2 and city[j][k] < 20:
                city[j][k] = 20

safe = 0

for i in range(r):
    for j in range(c):
        if not city[i][j]:
            safe += 1

print(safe)
print(str(city[x][y]) + "%")
