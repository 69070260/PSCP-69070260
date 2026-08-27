"""โปรแกรมคิดเงินสมาชิก"""

M = input()
n = int(input())

total = 0

for _ in range(n):
    total += float(input())

if M == "Y":
    total = total * 95 / 100
elif total >= 500:
    total = total * 97 / 100

total = int(total * 100 + 0.50000001) / 100

print(f"{total:.2f}")
