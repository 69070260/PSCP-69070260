"""โปรแกรม Meteorite"""

a = float(input())
b = int(input())
c = float(input())

count = 0
meteors = 1

while a >= c:
    count += meteors
    meteors *= b
    a /= b

print(count)
