"""โปรแกรม Coffe Shop"""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = int(input())

price1 = a + (e - 1) * a * (1 - b / 100)
price2 = a * e

if price2 >= d:
    price2 = price2 * (1 - c / 100)

if price1 < price2:
    print(1)
    print(f"{price1:.2f}")
else:
    print(2)
    print(f"{price2:.2f}")
