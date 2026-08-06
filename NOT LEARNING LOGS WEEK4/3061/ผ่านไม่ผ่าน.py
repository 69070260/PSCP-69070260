"""โปรแกรมคิดเกรดผ่าน/ไม่ผ่าน"""

mid = int(input())
final = int(input())

total = mid + final

print(total)

if total >= 50:
    print("pass")
else:
    print("fail")
