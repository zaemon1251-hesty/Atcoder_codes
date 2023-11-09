from math import pi, cos, sin
import numpy as np


def main():
    a, b, d = map(int, input().split())
    rad = d * pi / 180
    A = np.array([[cos(rad), -sin(rad)], [sin(rad), cos(rad)]])
    p0 = np.array([a, b])
    p1 = np.dot(A, p0)
    p1 = p1.tolist()
    print(*p1)


if __name__ == "__main__":
    main()
