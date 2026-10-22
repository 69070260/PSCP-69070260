"""โปรแกรม Coke อีกแล้ว"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d == 0:
    print(0)
elif b == 0 or c >= a:
    print(a * d)
elif b == 1:
    print(a + (d - 1) * c)
else:
    money = 0
    caps = 0
    bottles = 0

    while bottles < d:
        if caps >= b:
            money += c
            caps = caps - b + 1
        else:
            money += a
            caps += 1
        bottles += 1

    print(money)
