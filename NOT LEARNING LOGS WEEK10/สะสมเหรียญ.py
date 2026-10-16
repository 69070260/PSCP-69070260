"""โปรแกรม สะสมเหรียญ"""
n = int(input())

fire_total = 0
water_total = 0
earth_total = 0

for _ in range(n):
    data = input().split()

    fire1 = int(data[0])
    water1 = int(data[1])
    earth1 = int(data[2])
    fire2 = int(data[3])
    water2 = int(data[4])
    earth2 = int(data[5])

    fire_total += max(fire1, fire2)
    water_total += max(water1, water2)
    earth_total += max(earth1, earth2)

total = fire_total + water_total + earth_total

print("Total:", total)
print("Fire:", fire_total)
print("Water:", water_total)
print("Earth:", earth_total)

if fire_total > water_total + earth_total:
    print("Bonus: YES")
else:
    print("Bonus: NO")
