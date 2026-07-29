"""โปรแกรมคำนวนค่าต่างๆใน Bill"""

food = int(input())        #ราคาอาหาร เขียนเผื่อตัวเองลืม นะแจ๊ะ

if food <= 500:            #ราคาอาหารถ้าต่ำกว่าหรือเท่ากับ 500 service จะคิดเป็น 50 บาท อิอิ
    SERVICE = 50
elif food >= 10000:        #ราคาอาหารถ้ามากกว่าหรือเท่ากับ 10000 service จะคิดเป็น 1000 บาท อิอิ
    SERVICE = 1000
else:                      #ราคาอาหารที่อยู่ระหว่าง 500 , 10000 จะคิดราคา service ตามปกตินะจร๊ะะ
    SERVICE = food * 0.1

VAT = (food + SERVICE) * 0.07
TOTAL = food + SERVICE + VAT

print(f"{TOTAL:.2f}")
