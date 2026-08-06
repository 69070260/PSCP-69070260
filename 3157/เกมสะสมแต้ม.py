"""โปรแกรมการคำนวนแต้มของการกระทำ"""
def main():
    """คำนวนแต้มการกระทำ"""

    x = int(input())
    count = 0

    for _ in range(x):
        y = input()
        if y == "+":
            count += 10
        elif y == "-":
            count -= 5
    print(count)
main()
