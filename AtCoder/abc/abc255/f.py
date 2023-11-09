import sys

sys.setrecursionlimit(10**6)


def main():
    N = int(input())
    P = list(map(lambda x: int(x) - 1, input().split()))
    I = list(map(lambda x: int(x) - 1, input().split()))
    posI = {I[i]: i for i in range(N)}
    L = [-1] * N
    R = [-1] * N

    def struct(s, t, S, T):
        r = P[s]
        p = posI[r]
        if p < S or T < p:
            return False

        if p > S:
            left = P[s + 1]
            L[r] = left
            if not struct(s + 1, s + p - S, S, p - 1):
                return False
        if T > p:
            right = P[s + p - S + 1]
            R[r] = right
            if not struct(s + p - S + 1, t, p + 1, T):
                return False
        return True

    if P[0] != 0 or not struct(0, N - 1, 0, N - 1):
        print(-1)
    else:
        for l, r in zip(L, R):
            print(l + 1, r + 1)


if __name__ == "__main__":
    main()
