"""โปรแกรมวิเคราะห์ยอดขายร้านกาแฟ"""
n = int(input())

sales = []

for _ in range(n):
    x = int(input())
    sales.append(x)

total = sum(sales)
maximum = max(sales)
minimum = min(sales)
average = total / n

print(total)
print(maximum)
print(minimum)
print(f"{average:.1f}")
