"""โปรแกรมนับสระ"""

def main():
    """นับสระ"""
    count = int(input())
    list2 = ["A","E","I","O","U"]
    counts = 0

    for _ in range(0,count):
        x = input()
        if x in list2:
            counts +=1

    print(counts)
main()
