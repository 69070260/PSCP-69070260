"""โปรแกรมแลกเงิน"""

money = int(input())

coin_10 = money // 10
money = money % 10

coin_5 = money // 5
money = money % 5

coin_2 = money // 2
money = money % 2

coin_1 = money // 1
money = money % 1

print("10 =", coin_10)
print("5 =", coin_5)
print("2 =", coin_2)
print("1 =", coin_1)
