"""โปรแกรม 1132-Median"""
numbers = input().split(", ")
numbers = [float(x) for x in numbers]
numbers.sort()

n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print(f"{median:.2f}")
