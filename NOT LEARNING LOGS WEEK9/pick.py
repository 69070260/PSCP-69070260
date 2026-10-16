"""โปรแกรม Pick"""
numbers = input().split()
found = False

for i in range(len(numbers) - 1, -1, -1):
    n = int(numbers[i])
    if not n % 3 or not n % 5:
        print(n)
        found = True

if not found:
    print("Nope")
