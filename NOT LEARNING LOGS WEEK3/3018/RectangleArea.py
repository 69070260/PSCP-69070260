"""หาพื้นที่สี่เหลี่ยม A และ B ทับซ้อนกัน"""

xA, yA, wA, hA = map(int, input().split())
xB, yB, wB, hB = map(int, input().split())

left = max(xA, xB)
right = min(xA + wA, xB + wB)

bottom = max(yA, yB)
top = min(yA + hA, yB + hB)

overlap_width = right - left
overlap_height = top - bottom

if overlap_width <= 0 or overlap_height <= 0:
    print("no overlapping")
else:
    area = overlap_width * overlap_height
    print(area)
