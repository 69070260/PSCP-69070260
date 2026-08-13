"""โปรแกรมบอกว่าบ้านของเขาที่พิกัด (x, y) จะถูกท่วมในวินาทีที่เท่าใด"""

import math as m

S, N = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())

    area = 3.1416 * (x **2 + y **2)
    time = m.ceil(area / S)

    print(time)
