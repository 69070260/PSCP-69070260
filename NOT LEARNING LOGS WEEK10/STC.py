"""โปรแกรม STC"""
n = int(input())

for _ in range(n):
    data = input().split()
    plastic = float(data[0])
    can = float(data[1])
    glass = float(data[2])

    total = plastic + can + glass
    result = []

    if total > 50:
        result.append("Overloaded")
    if plastic > 20:
        result.append("Check Type Plastic")
    if can > 20:
        result.append("Check Type Can")
    if glass > 20:
        result.append("Check Type Glass")

    print(f"{total:.1f}", end="")
    if result:
        print(", " + ", ".join(result))
    else:
        print()
