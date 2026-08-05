"""โปรแกรมเปลี่ยนหน่วยอุณหภูมิเป็นหน่วย"""

x = float(input())
temp1 = input()
temp2 = input()

check = ["F","K","R"]

if temp2 in check:
    if temp2 in ("F"):
        print(f"{((x * 9/5) + (32)):.2f}")
    elif temp2 in ("K"):
        print(f"{(x + 273.15):.2f}")
    elif temp2 in ("R"):
        print(f"{(x + 273.15) * (9/5):.2f}")
