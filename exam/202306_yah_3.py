from __future__ import annotations
import sys
from collections import deque
from itertools import combinations
import numpy as np


def line_cross_point(P0, P1, Q0, Q1):
    x0, y0 = P0
    x1, y1 = P1
    x2, y2 = Q0
    x3, y3 = Q1
    a0 = x1 - x0
    b0 = y1 - y0
    a2 = x3 - x2
    b2 = y3 - y2

    d = a0 * b2 - a2 * b0
    if d == 0:
        # two lines are parallel
        return None

    sn = b2 * (x2 - x0) - a2 * (y2 - y0)
    return x0 + a0 * sn / d, y0 + b0 * sn / d


def in_rect(rect, target):
    a = (rect[0][0], rect[0][1])
    b = (rect[1][0], rect[1][1])
    c = (rect[2][0], rect[2][1])
    d = (rect[3][0], rect[3][1])
    e = (target[0], target[1])

    # 原点から点へのベクトルを求める
    vector_a = np.array(a)
    vector_b = np.array(b)
    vector_c = np.array(c)
    vector_d = np.array(d)
    vector_e = np.array(e)

    # 点から点へのベクトルを求める
    vector_ab = vector_b - vector_a
    vector_ae = vector_e - vector_a
    vector_bc = vector_c - vector_b
    vector_be = vector_e - vector_b
    vector_cd = vector_d - vector_c
    vector_ce = vector_e - vector_c
    vector_da = vector_a - vector_d
    vector_de = vector_e - vector_d

    # 外積を求める
    vector_cross_ab_ae = np.cross(vector_ab, vector_ae)
    vector_cross_bc_be = np.cross(vector_bc, vector_be)
    vector_cross_cd_ce = np.cross(vector_cd, vector_ce)
    vector_cross_da_de = np.cross(vector_da, vector_de)

    return vector_cross_ab_ae > 0 and vector_cross_bc_be > 0 and vector_cross_cd_ce > 0 and vector_cross_da_de > 0


def floatstr_to_int(floatstr: str) -> int:
    upper, lower = floatstr.split(".")
    return int(upper) * 100 + int(lower)


def parse(lines: deque[str]):
    n, lenght = map(float, lines.popleft().split())
    n = int(n)

    balicades = []
    for _ in range(n):
        a, b, c, d = map(floatstr_to_int, lines.popleft().split())
        balicades.append((a, b, c, d))

    return lenght, n, balicades


def get_quadrilateral(length, line_0, line_1) -> list[tuple[int, int]] | None:
    origin = (0, 0)
    x_sup = (length, 0)
    y_sup = (0, length)
    raise NotImplementedError


def main(lines: deque[str]):
    length, line_num, balicades = parse(lines)
    inf = 1 << 60
    ans = inf
    for i, j in combinations(range(line_num), 2):
        line_0 = balicades[i]
        line_1 = balicades[j]
        points = get_quadrilateral(length, line_0, line_1)
        if points is None:
            continue
        if in_rect(points, (length, length)):
            ans = min(ans, max(i + 1, j + 1))
    if ans != inf:
        print("NO")
        print(ans)
    else:
        print("YES")

    return


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(deque(lines))
