"""aaa"""
temp = float(input())
from_unit = input()
to_unit = input()

# เปลี่ยนหน่วยต้นทางให้เป็น Celsius ก่อน
if from_unit == "C":
    c = temp
elif from_unit == "F":
    c = (temp - 32) * 5 / 9
elif from_unit == "K":
    c = temp - 273.15
elif from_unit == "R":
    c = temp * 5 / 9 - 273.15

# เปลี่ยนจาก Celsius เป็นหน่วยที่ต้องการ
if to_unit == "C":
    result = c
elif to_unit == "F":
    result = c * 9 / 5 + 32
elif to_unit == "K":
    result = c + 273.15
elif to_unit == "R":
    result = (c + 273.15) * 9 / 5

print(f"{result:.2f}")