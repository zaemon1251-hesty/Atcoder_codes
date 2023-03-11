import sys
from itertools import product


MOD = 998244353


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = [li() for _ in range(N)]

    ans = [1, 1]

    for i in range(1, N):
        new_ans = [0, 0]
        for p0, p1 in product(range(2), repeat=2):
            if S[i - 1][p0] != S[i][p1]:
                new_ans[p1] += ans[p0]
                new_ans[p1] %= MOD
        ans = new_ans

    print(sum(ans) % MOD)


if __name__ == '__main__':
    main()
