"""โปรแกรม Align"""

size = int(input())
align = input()
text = input()

space = size - len(text)

if align == "left":
    result = text + " " * space
elif align == "right":
    result = " " * space + text
else:
    left = (space + 1) // 2
    right = space - left
    result = " " * left + text + " " * right

print(result)
