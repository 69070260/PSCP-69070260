"""Electric_Using"""
n = int(input())

if n <= 10:
    electricity = n * 5
elif n <= 50:
    electricity = 10 * 5 + (n - 10) * 7
elif n <= 100:
    electricity = 10 * 5 + 40 * 7 + (n - 50) * 10
elif n <= 200:
    electricity = 10 * 5 + 40 * 7 + 50 * 10 + (n - 100) * 12
else:
    electricity = 10 * 5 + 40 * 7 + 50 * 10 + 100 * 12 + (n - 200) * 15

ft = n * 0.50
vat = electricity * 0.07

total = electricity + ft + vat

total = int(total * 10 + 0.5) / 10

print(f"{total:.1f}")
