"""โปรแกรม PickThem"""
data = input().replace("[", "").replace("]", "").split(",")
found = False

for i in data:
    num = int(i)
    if not num % 2:
        print(num)
        found = True

if not found:
    print("Nope")
