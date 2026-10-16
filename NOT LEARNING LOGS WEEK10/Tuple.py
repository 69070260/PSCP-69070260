"""โปรแกรม Tuple"""
data = tuple(input().split())
target = input()

position = data.index(target)
count = data.count(target)

for _ in range(count):
    for j in range(count):
        if j > 0:
            print(" ", end="")
        print(position, end="")
    print()
