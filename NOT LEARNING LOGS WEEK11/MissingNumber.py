"""โปรแกรม MissingNumber"""
n = int(input())
numbers = []

while True:
    x = int(input())
    if not x:
        break
    numbers.append(x)

for i in range(1, n + 1):
    if i not in numbers:
        print(i)
