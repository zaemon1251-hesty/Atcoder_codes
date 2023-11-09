from functools import lru_cache
import sys
from typing import List, Tuple, Callable

sys.setrecursionlimit(10**6)

buf: List[Tuple[Callable, int]]


@lru_cache(None)
def dfs(x, i):
    if i == 0:
        return buf[i][0](x, buf[i][1])
    return buf[i][0](dfs(x, i - 1), buf[i][1])


def _or(x, y):
    return x | y


def _and(x, y):
    return x & y


def _xor(x, y):
    return x ^ y


ops = [None, _and, _or, _xor]


def parseOp(arr):
    return (ops[arr[0]], arr[1])


def main():
    N, C = map(int, input().split())
    buf = [list(map(int, input().split())) for _ in range(N)]
    buf = list(map(parseOp, buf))

    res = [0 for _ in range(N)]
    for k in range(30):
        ck = (C >> k) & 1
        synsfunc = [0, 1]
        for i in range(N):
            bit = (buf[i][1] >> k) & 1
            # calc f[i](f[i-1](...(f[1](x)))), {x in [0,1]}
            synsfunc = [buf[i][0](synsfunc[0], bit), buf[i][0](synsfunc[1], bit)]
            ck = synsfunc[ck]
            res[i] |= ck << k

    for d in res:
        print(d)


if __name__ == "__main__":
    main()
