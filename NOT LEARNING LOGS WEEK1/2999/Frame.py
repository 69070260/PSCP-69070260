"""รับค่า string มาแล้วให้มันแสดงในรูปกรอบสี่เหลี่ยม"""
NAME = str(input())

print("*" * (len(NAME) + 2))
print("*" + NAME + "*")
print("*" * (len(NAME) + 2))
