"""Conan"""
text = input()
k = int(input())

result = ""

for ch in text:
    new_ch = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    result += new_ch

print(result)
