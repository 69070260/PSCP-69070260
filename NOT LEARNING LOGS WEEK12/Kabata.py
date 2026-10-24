"""โปรแกรม Kabata"""

n = int(input())

for _ in range(n):
    s = input()
    i = 0
    valid = True

    while i < len(s):
        if s[i:i + 5] == "bakka":
            i += 5
        elif s[i:i + 2] == "ba":
            i += 2
            if s[i:i + 2] == "ka":
                valid = False
                break
        elif s[i:i + 2] == "ka" or s[i:i + 2] == "ta":
            i += 2
        else:
            valid = False
            break

    if valid:
        print("yes")
    else:
        print("no")
