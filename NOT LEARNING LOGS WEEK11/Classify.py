"""โปรแกรม Classify"""

students = {}

while True:
    code = input()

    if code == "END":
        break

    year = code[:2]
    faculty = str(int(code[2:4]))

    if year not in students:
        students[year] = {}

    if faculty not in students[year]:
        students[year][faculty] = 0

    students[year][faculty] += 1

for year in sorted(students):
    faculties = sorted(students[year], key=int)

    for i, faculty in enumerate(faculties):
        if not i:
            print(year, faculty, students[year][faculty])
        else:
            print("--", faculty, students[year][faculty])
