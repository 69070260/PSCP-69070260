"""โปรแกรมคำนวนการพังกำแพงไปหาเลข 1"""
def main():
    """คำนวนการพังกำแพงไปหาเลข 1"""
    n = int(input())

    if n == 1:
        print(0)
    else:
        layer = 1
        while layer * layer < n:
            layer += 1

        max_num = layer * layer
        side = layer - 1

        centers = [
            max_num - side // 2,
            max_num - side // 2 - side,
            max_num - side // 2 - side * 2,
            max_num - side // 2 - side * 3
        ]

        d1 = abs(n - centers[0])
        d2 = abs(n - centers[1])
        d3 = abs(n - centers[2])
        d4 = abs(n - centers[3])

        distance = d1

        if d2 < distance:
            distance = d2

        if d3 < distance:
            distance = d3

        if d4 < distance:
            distance = d4

        answer = side + distance

        print(answer)
main()
