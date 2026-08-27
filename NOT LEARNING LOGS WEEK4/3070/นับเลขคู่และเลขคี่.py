"""โปรแกรมเพื่อรับจำนวนเต็ม 3 ตัวจากแป้นพิมพ์ จากนั้นหาว่ามีเลขคู่และเลขคี่อยู่กี่ตัว"""

even = 0
odd = 0

for _ in range(3):
    n = int(input())

    if not n % 2:
        even += 1
    else:
        odd += 1

print(even)
print(odd)
