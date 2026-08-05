"""โปรแกรมคำนวนโปรโมชันCoke"""
a = int(input()) #ขวดละกี่บาท
b = int(input()) #จำนวนฝาที่เอามาแลกได้ตามโปร
c = int(input()) #ซื้อขวดใหม่ในราคาโปรกี่บาท
d = int(input()) #จะซื้อกี่ขวด

if not b or b > d:
    print(a * d)
elif b == 1:
    print(((d - 1) * c) + (1 * a))
else:
    first = (d - 1) // b
    left = (d - 1) % b
    print((first * (((b - 1) * a) + c)) + ((left * a) + a))
