from __future__ import annotations
import sys
from math import gcd
from functools import reduce


def main(argv: list[str]) -> None:
    if len(argv) < 3:
        raise Exception("引数が足りません")

    left, right, m = int(argv[0]), int(argv[1]), int(argv[2])

    if len(argv[3:]) != m:
        raise Exception("引数エラーです。mで指定した数だけ続けて入力してください")

    n = list(map(int, argv[3:]))

    result = solve(left, right, n)
    print(result)


def solve(left: int, right: int, n: list[int]):
    m = len(n)

    # 包除原理
    death_num = 0
    for i in range(1 << m):
        candidates = []
        for j in range(m):
            if i >> j & 1:
                candidates.append(n[j])

        # 何も選ばない場合はスキップ
        if len(candidates) == 0:
            continue

        lcm_value = lcm(candidates)
        death_num += (right // lcm_value - (left - 1) // lcm_value) * (-1) ** (len(candidates) - 1)

    # [left, right]からdeath_numを引く
    ans = right - left + 1 - death_num

    return ans


def lcm(x_list: list[int]) -> int:
    def _lcm(x: int, y: int) -> int:
        return (x * y) // gcd(x, y)

    return reduce(_lcm, x_list)


if __name__ == "__main__":
    main(sys.argv[1:])
