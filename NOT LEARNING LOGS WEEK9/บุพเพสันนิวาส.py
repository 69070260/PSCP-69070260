"""โปรแกรม บุพเพ"""

name1 = input()
name2 = input()

while len(name1) < len(name2):
    name1 += name1[0]
while len(name2) < len(name1):
    name2 += name2[0]

LOVE = "love"
yan = ""

for i, char in enumerate(name1):
    if char.lower() in LOVE or name2[i].lower() in LOVE:
        yan += "w"
    else:
        yan += "$"

COUNT = yan.count("w")

if COUNT % 2 == 1:
    max_w = 0
    current_w = 0

    for i, char in enumerate(yan):
        if char == "w":
            current_w += 1
            if current_w > max_w:
                max_w = current_w
        else:
            current_w = 0

    yan += str(max_w)
else:
    if "ww" not in yan:
        yan += "#"

print(yan)
