"""โปรแกรม OneTwo"""

n = int(input())

s1 = "1"
s2 = "2"

for _ in range(3, n + 1):
    s3 = s2 + s1
    s1 = s2
    s2 = s3

if n == 1:
    print("1")
else:
    print(s2)
