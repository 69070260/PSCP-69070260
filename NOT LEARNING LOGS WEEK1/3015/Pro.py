"""โปรแกรมคำนวณโปรโมชัน Buffet"""

x = int(input()) #มา4
y = int(input()) #จ่าย3
a = int(input()) #ราคาต่อหัว
z = int(input()) #จำนวนคนที่มา

if x >= y:
    print((z * a) - (z // y) * 100 )
