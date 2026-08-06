"""โปรแกรมคำนวนการออกกำลังกายตามที่saitamaบอก"""
pushup = int(input())
situp = int(input())
stand = int(input())
run = int(input())

day_pushup = int(input())
day_situp = int(input())
day_run = int(input())
day_stand = int(input())

x1 = (pushup + day_pushup - 1) // day_pushup
x2 = (situp + day_situp - 1) // day_situp
x3 = (stand + day_stand - 1) // day_stand
x4 = (run + day_run - 1) // day_run

print(max(x1, x2, x3, x4))
