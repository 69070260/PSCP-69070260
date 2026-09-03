"""ผ่านหรือไม่"""
n = int(input())

total = 0
passed_all = True

for _ in range(n):
    score = int(input())
    total += score

    if score < 50:
        passed_all = False

average = total / n

print(f"{average:.1f}")

if passed_all and average >= 60:
    print("PASS")
else:
    print("FAIL")
