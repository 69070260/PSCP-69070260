"""โปรแกรมหา Quadrant"""
x = int(input())
y = int(input())

if not x:
    if not y:
        print("O")
    else:
        print("Y")
elif not y:
    print("X")
elif x >= 1 and y >= 1:
    print("Q1")
elif x <= -1 and y >= 1:
    print("Q2")
elif x <= -1 and y <= -1:
    print("Q3")
elif x >= 1 and y <= -1:
    print("Q4")
