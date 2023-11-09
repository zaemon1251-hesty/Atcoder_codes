from collections import Counter
from itertools import combinations
import sys


def dist(x, y):
    return (y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    S = {}
    for i in range(9):
        s = input()
        for j in range(9):
            S[i, j] = s[j]

    ans = 0
    for a, b, c, d in combinations(range(81), 4):
        if any(S[divmod(z, 9)] == "." for z in (a, b, c, d)):
            continue
        s = [
            dist(divmod(a, 9), divmod(b, 9)),
            dist(divmod(b, 9), divmod(c, 9)),
            dist(divmod(c, 9), divmod(d, 9)),
            dist(divmod(d, 9), divmod(a, 9)),
            dist(divmod(a, 9), divmod(c, 9)),
            dist(divmod(b, 9), divmod(d, 9)),
        ]
        cnts = Counter(s)
        if len(cnts) == 2 and sorted(cnts.values()) == [2, 4]:
            cross, edge = 0, 0
            for k, v in cnts.items():
                if v == 2:
                    cross = k
                else:
                    edge = k
            if cross == 2 * edge:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
