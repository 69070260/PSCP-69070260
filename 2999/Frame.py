"""รับค่า string มาแล้วให้มันแสดงในรูปกรอบสี่เหลี่ยม"""
name = str(input())

print("*" * (len(name) + 2))
print("*" + name + "*")
print("*" * (len(name) + 2))
