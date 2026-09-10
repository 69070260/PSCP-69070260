"""Elon"""
#ข้อนี้ผมใช้ AI ผมไม่ไหวแล้วครับ T^T

x, k = input().split()
x = int(x)

for i in range(x):
    for j in range(x):
        if j == i or j == x - 1 - i:
            if k == "#":
                print("#", end="")
            else:
                d = abs(x // 2 - i)
                print(chr(ord(k) + d), end="")
        else:
            print("-", end="")
    print()
