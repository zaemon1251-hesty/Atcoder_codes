from math import pi, cos, sin
import numpy as np


def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())
    xm, ym = (x0 + xn2) / 2, (y0 + yn2) / 2
    A = np.array([[cos(2 * pi / N), -sin(2 * pi / N)], [sin(2 * pi / N), cos(2 * pi / N)]])
    p0 = np.array([x0, y0])
    pm = np.array([xm, ym])
    p1 = np.dot(A, p0 - pm) + pm
    p1 = p1.tolist()
    print(*p1)


if __name__ == "__main__":
    main()
