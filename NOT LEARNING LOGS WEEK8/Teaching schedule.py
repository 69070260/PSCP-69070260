"""Teaching schedule"""
N = int(input())
A = int(input())

total = N * A

if not total:
    print("No teaching")
elif total < 60:
    print(total, "minute")
elif not total % 60:
    print(total // 60, "hours")
else:
    print(total // 60, "hours", total % 60, "minute")
