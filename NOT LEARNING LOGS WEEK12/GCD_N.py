"""โปรแกรม GCD_N"""

n = int(input())
gcd = int(input())

for _ in range(n - 1):
    num = int(input())

    while num != gcd:
        if num > gcd:
            num -= gcd
        else:
            gcd -= num

print(gcd)
