"""โปรแกรมใส่กล่อง"""
W, L, M, N = map(int, input().split())

answer = W * L

for A in range(M, N + 1):
    used = A * (W // A) * L
    used += A * (W % A) * (L // A)

    waste = W * L - used

    if waste < answer:
        answer = waste

print(answer)
