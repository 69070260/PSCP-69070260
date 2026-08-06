"""โปรแกรมคำนวนหาความพอดีของกระดาษที่จะเอามาห่อของขวัญ"""

pie = float(3.14)
r, h, glue = map(float, input().split())

width = (2 * pie * r) + glue
length = h + (2 * r)

print(f"{length:.2f} {width:.2f}")
