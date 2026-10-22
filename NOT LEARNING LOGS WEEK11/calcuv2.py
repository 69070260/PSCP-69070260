"""โปรแกรม cal2"""

n = int(input())

S = str(n)
digits = 0

for i in range(len(S)):
    digits += (i + 1) * 9 * (10 ** i)

digits = 0
for i in range(1, len(S)):
    digits += i * 9 * (10 ** (i - 1))

digits += len(S) * (n - 10 ** (len(S) - 1) + 1)

if n == 1:
    print(1)
else:
    print(digits + n)
