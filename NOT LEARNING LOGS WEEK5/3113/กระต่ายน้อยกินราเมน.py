"""โปรแกรมคำนวณกระต่ายกินราเมน"""

size, ramen = input().split()
topping = input().split()

if size == "S":
    if ramen == "R":
        price = 60
    else:
        price = 80
elif size == "M":
    if ramen == "R":
        price = 80
    else:
        price = 100
else:
    if ramen == "R":
        price = 100
    else:
        price = 120

if topping[0] == "P":
    price += int(topping[1]) * 15
elif topping[0] == "E":
    price += int(topping[1]) * 10

print(price)
