from math import cos, pi, sqrt
A, B, H, M = map(int, input().split())
theta = pi * abs(60 * H - 11 * M)/12/30
if theta > pi:
    theta = 2 * pi - theta
print(sqrt(A**2 + B**2 - 2 * A * B * cos(theta)))
