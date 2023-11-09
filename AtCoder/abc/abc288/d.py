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

    N, K = mi()
    A = li()
    cum = [[0] * (N + 1) for _ in range(K)]

    for j in range(K):
        for i in range(N):
            cum[j][i + 1] += cum[j][i] + int(i % K == j) * A[i]

    def get(j, L, r):
        return cum[j][r] - cum[j][L]

    Q = ii()
    for _ in range(Q):
        L, R = mi()
        L -= 1
        val = get(0, L, R)
        same = True
        for j in range(1, K):
            same &= val == get(j, L, R)
        print("Yes" if same else "No")


if __name__ == "__main__":
    main()
