"""โปรแกรมเปลี่ยนหน่วยอุณหภูมิเป็นหน่วย"""

x = float(input())
temp1 = input()
temp2 = input()

check = ["C","F","K","R"]

if temp1 in check:
    if temp1 in ("C") and temp2 in ("F"):
        print(f"{((x * 9/5) + (32)):.2f}")
    elif temp1 in ("C") and temp2 in ("K"):
        print(f"{(x + 273.15):.2f}")
    elif temp1 in ("C") and temp2 in ("R"):
        print(f"{(x + 273.15) * (9/5):.2f}")
    elif temp1 in ("F") and temp2 in ("C"):
        print(f"{((x - 32) * 5 / 9):.2f}")
    elif temp1 in ("F") and temp2 in ("K"):
        print(f"{(x - 32) * (5/9) + 273.15:.2f}")
    elif temp1 in ("F") and temp2 in ("R"):
        print(f"{x + 459.67:.2f}")
    elif temp1 in ("K") and temp2 in ("C"):
        print(f"{x - 273.15:.2f}")
    elif temp1 in ("K") and temp2 in ("F"):
        print(f"{(x - 273.15) * (9/5) + 32:.2f}")
    elif temp1 in ("K") and temp2 in ("R"):
        print(f"{(x * (9 / 5)):.2f}")
    elif temp1 in ("R") and temp2 in ("C"):
        print(f"{(x - 491.67) * (5 / 9):.2f}")
    elif temp1 in ("R") and temp2 in ("F"):
        print(f"{x - 459.67:.2f}")
    elif temp1 in ("R") and temp2 in ("K"):
        print(f"{x * (5 / 9):.2f}")
    elif temp1 == temp2:
        print(f"{x:.2f}")
