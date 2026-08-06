"""โปรแกรมหาค่าน้อยสุด"""

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(a)
elif (a <= b) and (a <= c):
    if a < c or a < b:
        print(a)
    elif a > c:
        print(c)
    elif a > b:
        print(b)
elif (b <= a) and (b <= c):
    if b < c or b < a:
        print(b)
    elif b > c:
        print(c)
    elif b > a:
        print(a)
elif (c <= a) and (c <= b):
    print(c)
