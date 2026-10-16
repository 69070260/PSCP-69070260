"""โปรแกรม Array"""
data = [0] * 50

for i in range(3):
    data[i] = int(input())
    print("Input number", i + 1, "stored.")

done = [False] * 4

while True:
    menu = int(input())

    if menu == 0:
        break

    if menu < 1 or menu > 3:
        continue

    if done[menu]:
        continue

    done[menu] = True

    if menu == 1:
        print("Original order:", *data[:3])
    elif menu == 2:
        print("Descending order:", *sorted(data[:3], reverse=True))
    elif menu == 3:
        print("Ascending order:", *sorted(data[:3]))
