"""โปรแกรมการหาจำนวนครั้งในการกดเครื่องคิดเลข"""

n = int(input())

if n == 1:
    print(1)
else:
    count = 0
    for i in range(1,n+1):
        count += len(str(i))
    count += (n-1)
    count += 1
    print(count)
    