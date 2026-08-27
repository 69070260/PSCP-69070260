"""โปรแกรมคํานวณค่าแท็กซี่เบื้องต้น"""

distance = int(input())

if not distance:
    PRICE = 0
elif distance <= 1:
    PRICE = 35
elif distance <= 10:
    PRICE = 35 + (distance - 1) * 5
else:
    PRICE = 35 + 9 * 5 + (distance - 10) * 8

print(PRICE)
