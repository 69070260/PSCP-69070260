"""ฟิลเตอร์ AR TikTok"""
r, x, y = map(float, input().split())

circle = x**2 + y**2
r_2 = r**2

if circle < r_2:
    print("IN")
elif circle == r_2:
    print("ON")
elif circle > r_2:
    print("OUT")
