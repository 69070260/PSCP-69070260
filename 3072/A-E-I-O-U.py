"""โปรแกรมนับสระ"""

def main():
    """นับสระ"""

    text = input()

    vowel = ["a", "e", "i", "o", "u"]
    count = [0, 0, 0, 0, 0]

    for ch in text:
        if ch in ("a","A"):
            count[0] += 1
        elif ch in ("e","E"):
            count[1] += 1
        elif ch in ("i","I"):
            count[2] += 1
        elif ch in ("o","O"):
            count[3] += 1
        elif ch in ("u","U"):
            count[4] += 1

    for i in range(5):
        if count[i] > 0:
            print(vowel[i], ":", count[i])

main()
