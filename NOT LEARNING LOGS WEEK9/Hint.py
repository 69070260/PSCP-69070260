"""โปรแกรม Hint"""

a = input().split()
b = input().split()
c = input().split()


def check(x, op, y):
    """Check the comparison between x and y."""
    if op == "==":
        return x == y
    if op == ">":
        return x > y
    if op == "<":
        return x < y
    if op == "<=":
        return x <= y
    if op == ">=":
        return x >= y
    if op == "!=":
        return x != y
    return False


for i in range(10):
    for j in range(10):
        for k in range(10):
            if (check(k, a[0], int(a[1])) and
                    check(j, b[0], int(b[1])) and
                    check(i, c[0], int(c[1]))):
                print(str(i) + str(j) + str(k))
