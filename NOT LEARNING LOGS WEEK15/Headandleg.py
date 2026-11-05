"""โปรแกรมนับหัว"""
a = int(input())
b = int(input())

rabbit = (b - 2 * a) // 2
bird = a - rabbit

if b < 2 * a or b > 4 * a or b % 2:
    print("Impossible")
else:
    print(rabbit, bird)
