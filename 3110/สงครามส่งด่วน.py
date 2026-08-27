"""โปรแกรมคํานวณค่าธรรมเนียมการส่งพัสดุจะต้องเลือกต้นทาง - ปลายทาง และ
น้ำหนักของพัสดุที่จะส่ง"""

route = input().split()
weight = float(input())

start = route[0]
end = route[1]

if start == "BKK" and end == "CNX":
    price = 10 + weight * 30
    print(f"{price:.2f}")
elif start == "CNX" and end == "UBP":
    price = 15 + weight * 40
    print(f"{price:.2f}")
elif start == "UBP" and end == "BKK":
    price = 20 + weight * 40
    print(f"{price:.2f}")
elif start == "BKK" and end == "PKT":
    price = 25 + weight * 50
    print(f"{price:.2f}")
elif start == "PKT" and end == "CNX":
    price = 30 + weight * 60
    print(f"{price:.2f}")
elif start == "UBP" and end == "PKT":
    price = 40 + weight * 70
    print(f"{price:.2f}")
else:
    print("Error")
