import math

x1, y1, r1 = map(int, input("Enter x1, y1, r1: ").split())
x2, y2, r2 = map(int, input("Enter x2, y2, r2: ").split())

dist = math.hypot(x1 - x2, y1 - y2)
if dist == r1 + r2 or dist == abs(r1 - r2):
    print("Circles touch each other.")
else:
    print("Circles do not touch.")
