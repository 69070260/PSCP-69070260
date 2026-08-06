"""โปรแกรม ให้คะแนนและตรวจคะแนนสูงสุดกับต่ำสุดห่างกัน 2"""
total = float(input())
high = float(input())

low = total - high - high

if low < 0:
    low = 0

d = high - low

if d > 2:
    print("Surprising")
else:
    print("Not surprising")
