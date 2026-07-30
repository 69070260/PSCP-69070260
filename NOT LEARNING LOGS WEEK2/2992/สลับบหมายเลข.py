"""โปรแกรมสลับหมายเลข"""

x = input()
y = input()
z = int(x[::-1])

if y == "+":
    print(f"{x} + {z} = {int(x) + int(z)}")
elif y == "*":
    print(f"{x} * {z} = {int(x) * int(z)}")
