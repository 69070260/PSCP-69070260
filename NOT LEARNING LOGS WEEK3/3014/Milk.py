"""โปรแกรมขายนม"""

a = int(input()) #ราคานมต่อขวด
b = int(input()) #จำนวนฝาขวดที่ตามโปร
c = int(input()) #เอาฝามาแรกนมได้กี่ขวด
d = int(input()) #มีเงินในตัวกี่บาท

milk = d//a

if b > 0:
    fa = milk
    while fa >= b:
        new_milk = (fa // b) * c
        milk += new_milk
        fa = (fa % b) + new_milk

print(milk)
