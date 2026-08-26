"""โปรแกรมคำนวนว่าใครเกิดก่อน"""

y1 = int(input())
m1 = int(input())
d1 = int(input())

y2 = int(input())
m2 = int(input())
d2 = int(input())

day1 = y1 * 365 + m1 * 30 + d1
day2 = y2 * 365 + m2 * 30 + d2

diff = day1 - day2

if -7 <= diff <= 7:
    print(0)
elif diff < 0:
    print(1)
else:
    print(2)
