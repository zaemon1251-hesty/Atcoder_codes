from bisect import bisect_left
from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    Rs = defaultdict(list)
    Cs = defaultdict(list)
    H, W, rs, cs = mi()
    N = ii()
    walls = [li() for _ in range(N)]
    Q = ii()
    queue = [input().split() for _ in range(Q)]

    for r, c in walls:
        Rs[r].append(c)
        Cs[c].append(r)

    for r in Rs:
        Rs[r].sort()
    for c in Cs:
        Cs[c].sort()

    cur = [rs, cs]

    for d, l in queue:
        r, c = cur
        ll = int(l)
        if d == "L":
            idx = bisect_left(Rs[r], c)
            if idx == 0:
                c = max(1, c - ll)
            else:
                c = max(Rs[r][idx - 1] + 1, c - ll)
        elif d == "R":
            idx = bisect_left(Rs[r], c)
            if idx == len(Rs[r]):
                c = min(W, c + ll)
            else:
                c = min(Rs[r][idx] - 1, c + ll)
        elif d == "U":
            idx = bisect_left(Cs[c], r)
            if idx == 0:
                r = max(1, r - ll)
            else:
                r = max(Cs[c][idx - 1] + 1, r - ll)
        else:
            idx = bisect_left(Cs[c], r)
            if idx == len(Cs[c]):
                r = min(H, r + ll)
            else:
                r = min(Cs[c][idx] - 1, r + ll)

        print(r, c)
        cur = [r, c]


if __name__ == "__main__":
    main()
