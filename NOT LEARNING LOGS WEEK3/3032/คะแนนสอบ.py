"""โปรแกรมหาว่าคนที่ได้คะแนนมากสุด (ได้ top) ได้คะแนนเท่าไหร่ และมีคน top กี่คน"""
def main():
    """คำนวนคะแนนสูงสุดและนับคนที่ได้คะแนนสูงสุด"""
    rabbit = int(input())
    highest = 0
    count = 0

    for _ in range(rabbit):
        score = int(input())
        if score > highest:
            highest = score
            count = 1
        elif score == highest:
            count += 1

    print(highest)
    print(count)

main()
