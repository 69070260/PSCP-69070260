"""โปรแกรมหาสถานะของน้ำ"""

def main():
    """ตรวจstrและคำนวนองศาไปองศาต่างๆ"""
    c = int(input())
    temp = input()
    check = ["C","c","F","f"]

    if temp in check:
        if temp in ("C","c"):
            if c <= 0:
                print("solid")
            elif c >= 100:
                print("gas")
            else:
                print("liquid")
        elif temp in ('F', 'f'):
            if c <= 32:
                print("solid")
            elif c >= 212:
                print("gas")
            else:
                print("liquid")

main()
