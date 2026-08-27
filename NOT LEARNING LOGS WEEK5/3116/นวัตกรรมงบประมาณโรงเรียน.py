"""โปรแกรมหานวัตกรรมงบประมาณโรงเรียน"""

school = input()

first = ord(school[0])
last = ord(school[-1])
length = len(school)

data = []

for i in range(10):
    if (i + 1) % 2 == 1:
        value = first + i
    else:
        value = last - i

    value = value % length
    value = value % 10

    data.append(value)

for i in range(2, 8):
    print(data[i], end=" ")
