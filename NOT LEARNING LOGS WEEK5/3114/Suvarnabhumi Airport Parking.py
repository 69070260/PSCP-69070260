"""โปรแกรม เพื่อคํานวณอัตราค่าจอดรถที่สนามบินสุวรรณภูมิ"""

start = input()
end = input()

h1, m1 = map(int, start.split("."))
h2, m2 = map(int, end.split("."))

start_min = h1 * 60 + m1
end_min = h2 * 60 + m2

diff = end_min - start_min

if diff < 0 or h1 > 23 or h2 > 23 or m1 > 59 or m2 > 59:
    print("ERROR")
elif diff <= 15:
    print("FREE")
else:
    hours = (diff + 59) // 60

    if hours == 1:
        print(25)
    elif hours == 2:
        print(50)
    elif hours == 3:
        print(80)
    elif hours == 4:
        print(110)
    elif hours == 5:
        print(145)
    elif hours == 6:
        print(180)
    elif hours <= 24:
        print(250)
    else:
        print("ERROR")
