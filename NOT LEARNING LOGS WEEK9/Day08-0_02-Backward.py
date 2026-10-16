"""โปรแกรม Day08-0_02-Backward"""
data = []

while True:
    text = input()
    if text == "NULL":
        break
    data.append(text)

for i in range(len(data) - 1, -1, -1):
    print(data[i])
