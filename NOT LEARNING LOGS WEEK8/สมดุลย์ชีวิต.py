"""โปรแกรมสมดุลย์ชีวิต"""

n = int(input())

long = 0
short = 0

for _ in range(n):
    h = int(input())

    if h > 18:
        long += 1
    else:
        short += 1

answer = n

if long > short + 1:
    answer += long - short - 1

print(answer)
