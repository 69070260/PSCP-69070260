"""โปรแกรมคิดราคาตั๋ว"""

age = int(input())
stat = input()

if age < 18 or stat in ("s","S"):
    print(int(20))
else:
    print(int(50))
