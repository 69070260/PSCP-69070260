"""โปรแกรมช่วยกระต่ายน้อยคำนวณว่าต้องซื้อลวดหนามยาวกี่เมตร และต้องจ่ายเงินกี่บาท"""

width , length , floor = map(int, input().split())   #กว้าง ยาว ชั้น
price = int(input())


print((2 * (width + length)) * floor)
print(((2 * (width + length)) * floor) * price)
