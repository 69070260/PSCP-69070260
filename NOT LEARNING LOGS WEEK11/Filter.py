"""โปรแกรม Filter"""
def main():
    """Filter students by score and display sorted student IDs."""
    data = input().strip()
    data = data[1:-1]
    pairs = data.split(",")
    students = {}

    for pair in pairs:
        key, value = pair.split(":")
        key = key.strip().strip("'").strip('"')
        students[key] = float(value)

    score = float(input())
    found = False

    for key in sorted(students):
        if students[key] >= score:
            print(key + "\t" + format(students[key], ".2f"))
            found = True

    if not found:
        print("Nope")

main()
