"""การเขียนโปรแกรมเพื่อคำนวณระยะทางแบบยูคลิดใน 2 มิติ"""
import math as m

q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())

d = m.sqrt((q1-p1)**2 + (q2-p2)**2)

print(d)
