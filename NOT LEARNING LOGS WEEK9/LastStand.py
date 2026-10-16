"""โปรแกรม"""
numbers = input().replace("[", "").replace("]", "").split(",")

for i in numbers:
    print(int(i) % 10)
