"""โปรแกรมถอนเงินจากเครื่อง ATM ที่บรรจุธนบัตร 1000 บาท 500 บาท และ 100 บาท"""
money = int(input())

if money < 100 or money > 20000 or money % 100:
    print("ERROR")
else:
    n1000 = money // 1000
    money %= 1000

    n500 = money // 500
    money %= 500

    n100 = money // 100

    if n1000 > 0:
        print("1000 =", n1000)
    if n500 > 0:
        print("500 =", n500)
    if n100 > 0:
        print("100 =", n100)
