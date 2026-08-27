"""โปรแกรมชานมไข่มุก"""

bubble, gram = input().split()
gram = int(gram)

tea, sweet, cc = input().split()
sweet = int(sweet)
cc = int(cc)

if bubble == "H":
    bubble_cal = 5
elif bubble == "O":
    bubble_cal = 3
else:
    bubble_cal = 2

if tea == "R":
    if sweet == 1:
        tea_cal = 12
    elif sweet == 2:
        tea_cal = 18
    else:
        tea_cal = 25
elif tea == "T":
    if sweet == 1:
        tea_cal = 15
    elif sweet == 2:
        tea_cal = 20
    else:
        tea_cal = 30
else:
    if sweet == 1:
        tea_cal = 10
    elif sweet == 2:
        tea_cal = 15
    else:
        tea_cal = 20

print(bubble_cal * gram + tea_cal * cc)
