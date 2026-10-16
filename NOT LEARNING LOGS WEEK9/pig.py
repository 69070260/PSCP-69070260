"""โปรแกรม Pig"""
n = int(input())
w = input().split()

total = 0
for i in range(n):
    a = int(w[i * 2])
    b = int(w[i * 2 + 1])

    if a > b:
        x = a
    else:
        x = b

    total += x

    if not i:
        RESULT = str(x)
    else:
        RESULT = RESULT + " + " + str(x)

if n == 1:
    print(total)
else:
    print(RESULT + " = " + str(total))
