"""กบน้อยกระโดด"""

data = input().split()

x = int(data[0])
y = int(data[1])

total = 0
count = 0
jump = x

while total < y and jump > 0:
    total += jump
    count += 1
    jump -= 2

if total >= y:
    print(count)
else:
    print(-1)
