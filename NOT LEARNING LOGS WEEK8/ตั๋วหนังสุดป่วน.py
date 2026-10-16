"""โปรแกรมตั๋วหนังสุดป่วน"""
seat = int(input())

while seat > 0:
    data = input()

    if not data:
        break

    age, ticket = map(int, data.split())

    if age < 15:
        print(-1)
    elif ticket > seat:
        print(-2)
    else:
        if age >= 15 and age <= 22:
            PRICE = 120
        elif age >= 60:
            PRICE = 75
        else:
            PRICE = 150

        total = PRICE * ticket
        seat -= ticket

        print(total, seat)
