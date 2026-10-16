"""โปรแกรม 113"""
text = input()

while "113" in text:
    text = text.replace("113", "", 1)

print(text)
