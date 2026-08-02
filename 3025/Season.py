"""โปรแกรมแสดงฤดูกาล"""
month = int(input())
day = int(input())

if month <= 2:
    print("winter")
elif month == 3 and day < 21:
    print("winter")
elif month == 3 and day >= 21:
    print("spring")
elif month <= 5:
    print("spring")
elif month == 6 and day < 21:
    print("spring")
elif month == 6 and day >= 21:
    print("summer")
elif month <= 8:
    print("summer")
elif month == 9 and day < 21:
    print("summer")
elif month == 9 and day >= 21:
    print("fall")
elif month <= 11:
    print("fall")
elif month == 12 and day < 21:
    print("fall")
elif month == 12 and day >= 21:
    print("winter")
