"""โรงแรมกลางกรุง"""
N = input()

a = int(N[0])
b = int(N[1])
c = int(N[2])
d = int(N[3])
e = int(N[4])

if a > 5:
    FIRST = 9
elif b > 5:
    FIRST = 10
elif c > 5:
    FIRST = 11
elif d > 5:
    FIRST = 12
elif e > 5:
    FIRST = 14
else:
    FIRST = 13

if N == N[::-1]:
    if a + e > 5:
        SECOND = 1
    elif b * d > 5:
        SECOND = 2
    else:
        SECOND = 0
else:
    if e and a // e > 5:
        SECOND = 1
    elif b - e > 5:
        SECOND = 2
    else:
        SECOND = 0

total = a + b + c + d + e
product = a * b * c * d * e

if total > 25:
    THIRD = 1
elif product > 55:
    THIRD = 2
else:
    THIRD = 0

print(str(FIRST) + str(SECOND) + str(THIRD))
