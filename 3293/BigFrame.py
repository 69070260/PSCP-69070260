"""โปรแกรม BigFrame"""

a = input()
b = input()
c = input()
d = input()
e = input()

m = max(len(a), len(b), len(c), len(d), len(e))

print("*" * (m + 4))
print("* " + a + " " * (m - len(a)) + " *")
print("* " + b + " " * (m - len(b)) + " *")
print("* " + c + " " * (m - len(c)) + " *")
print("* " + d + " " * (m - len(d)) + " *")
print("* " + e + " " * (m - len(e)) + " *")
print("*" * (m + 4))
