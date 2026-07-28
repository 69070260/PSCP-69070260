"""ฝึกเขียน if"""
try:
    score = int(input("โปรดป้อนคะแนนของคุณ: "))

    if score >= 50 and score < 55:
        print("D")
    elif score >= 55 and score < 60:
        print("D+")
    elif score >= 60 and score < 65:
        print("C")
    elif score >= 65 and score < 70:
        print("C+")
    elif score >= 70 and score < 75:
        print("B")
    elif score >= 75 and score < 80:
        print("B+")
    elif score >= 80:
        print("A")
    elif score < 50:
        print("F")

except ValueError:
    print("ข้อมูลผิดพลาด โปรดดำเนินการใหม่อีกครั้ง")

#_______________________________________________________________#

while True:
    try:
        score = int(input("โปรดป้อนคะแนนของคุณ: "))

        if 0 <= score <= 100:
            break
        else:
            print("คะแนนต้องอยู่ระหว่าง 0-100")

    except ValueError:
        print("ข้อมูลผิดพลาด โปรดดำเนินการใหม่อีกครั้ง")

if score >= 80:
    print("A")
elif score >= 75:
    print("B+")
elif score >= 70:
    print("B")
elif score >= 65:
    print("C+")
elif score >= 60:
    print("C")
elif score >= 55:
    print("D+")
elif score >= 50:
    print("D")
else:
    print("F")
