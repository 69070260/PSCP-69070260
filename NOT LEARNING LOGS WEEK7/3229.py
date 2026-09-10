"""ระบบคิดคะแนนเกมออนไลน์"""

base = int(input())
bonus = int(input())
day = int(input())

total = base + bonus

if day > 3:
    total = total * 1.5

if total >= 1500:
    RANK = 5
elif total >= 1000:
    RANK = 4
elif total >= 500:
    RANK = 3
elif total >= 200:
    RANK = 2
elif total < 200:
    RANK = 1
else:
    RANK = 0

if RANK == 5 and day >= 7:
    SP = 99
elif RANK == 4 and bonus > 300:
    SP = 88
else:
    SP = 0

print(int(total))
print(RANK)
print(SP)
