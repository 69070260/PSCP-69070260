"""โปรแกรม Ball"""
n = float(input())
count = 0

while n * 0.6 >= 0.01:
    n = n * 0.6
    count += 1

print(count)
