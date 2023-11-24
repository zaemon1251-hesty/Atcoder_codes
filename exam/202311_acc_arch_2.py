from __future__ import annotations
import sys
from itertools import product


def main(lines):
    square_length, query_number, queries = parse_args(lines)
    coodinates = [["."] * square_length for _ in range(square_length)]

    last_coodinates = solve(square_length, queries, coodinates)
    print(*["".join(cood) for cood in last_coodinates], sep="\n")


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solve(n: int, Q: list[tuple[int, int]], G: list[list[int]]) -> int:
    painted_mass_number = 0
    for r, c, k in Q:
        # 0-indexed に変換
        r -= 1
        c -= 1

        # 全部塗りつぶされていたら終了
        if painted_mass_number == n * n:
            break

        for i, j in product(range(n), repeat=2):
            if G[i][j] == "#":
                continue
            if dist(r, c, i, j) <= k:
                G[i][j] = "#"
                painted_mass_number += 1
    return G


def parse_args(lines) -> tuple[int, int, list[tuple[int, int]]]:
    square_length = int(lines[0])
    query_number = int(lines[1])
    queries = []
    for line in lines[2:]:
        queries.append(tuple(map(int, line.split())))
    return square_length, query_number, queries


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
