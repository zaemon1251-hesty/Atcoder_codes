import math
a, b, x = map(int, input().split())
def angle(x):
    return math.atan(x) * 180 / math.pi
pre = 2 * (a**2 * b - x) / a**3
pro = a * b * b / x / 2
jd = 2 * x / a**3
if jd > b / a:
    print(angle(pre))
else:
    print(angle(pro))
