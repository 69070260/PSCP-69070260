"""โปรแกรมไทยช่วยไทย"""
x1 = input() #ชื่อผู้ลงทะเบียน
x2 = int(input()) #อายุ
x3 = int(input()) #รายได้ต่อเดือน
x4 = input() #Y N
x5 = int(input()) #จำนวนคนที่ต้องดูแล

if 1 <= x2 < 18:
    print(x1, "NOT ELIGIBLE")
elif 18 <= x2 <= 120:
    if x4 == "Y":
        rank = "GOLD"
        money = 3000
        if x5 >= 3:
            money_spe = 500
            print(x1, "GOLD", money+money_spe)
        else:
            money_spe = 0
            print(x1, "GOLD", money+money_spe)
    elif x4 == "N":
        if 0 <= x3 <= 15000:
            rank = "GOLD"
            money = 3000
            if x5 >= 3:
                money_spe = 500
                print(x1, "GOLD", money+money_spe)
            else:
                money_spe = 0
                print(x1, "GOLD", money+money_spe)
        elif 15000 < x3 <= 30000:
            rank = "SILVER"
            money = 1500
            if x5 >= 3:
                money_spe = 500
                print(x1, "SILVER", money+money_spe)
            else:
                money_spe = 0
                print(x1, "SILVER", money+money_spe)
        else:
            print(x1, "NOT ELIGIBLE")
    else:
        print(x1, "NOT ELIGIBLE")
else:
    print(x1, "NOT ELIGIBLE")
