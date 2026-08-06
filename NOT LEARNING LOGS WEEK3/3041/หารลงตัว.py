"""โปรแกรมหารลงตัว"""

num1 = int(input())
num2 = int(input())

if not num2:
    print("no")
elif not num1 % num2:
    print("yes")
else:
    print("no")
