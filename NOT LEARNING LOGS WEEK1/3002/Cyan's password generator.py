"""เขียนโปรแกรมเพื่อรับชื่อนามสกุลเอามาบางตัว"""

name = input()
surname = input()
age = input()

n = len(name)
s = len(surname)
if n >= 5 and s >= 5:
    print(name[0:2] + surname[-1] + age[-1])
else:
    print(name[0] + age + surname[-1])
