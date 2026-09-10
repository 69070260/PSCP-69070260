"""โปรแกรมสลากกินแบ่ง"""

result = input().split()
buy = input().split()

result_letter = result[0]
result_num = result[1]

buy_letter = buy[0]
buy_num = buy[1]

if result_letter == buy_letter and result_num == buy_num:
    print(1000000)

elif result_num == buy_num:
    print(100000)

elif result_letter == buy_letter and result_num[-3:] == buy_num[-3:]:
    print(2000)

elif result_letter == buy_letter and result_num[-2:] == buy_num[-2:]:
    print(1000)

elif result_num[-3:] == buy_num[-3:]:
    print(200)

elif result_num[-2:] == buy_num[-2:]:
    print(100)

elif result_letter == buy_letter:
    print(20)

else:
    print(0)
