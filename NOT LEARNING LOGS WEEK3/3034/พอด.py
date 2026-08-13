"""โปรแกรมคำนวนคนรอพอด"""
def main():
    """คำนวนคนรอพอด"""
    N, K = map(int, input().split())

    q = [0] * K

    for _ in range(N):
        x = int(input())
        q[x - 1] += 1

    minimum = min(q)

    answer = N - (minimum * K)

    print(answer)

main()
