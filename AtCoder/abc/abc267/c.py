from itertools import accumulate
from math import inf


def main():
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    S = list(accumulate(A))
    res = sum(i * A[i] for i in range(1, M + 1))
    ans = res
    for i in range(M + 1, N + 1):
        res += A[i] * M - (S[i - 1] - S[i - 1 - M])
        ans = max(res, ans)
    print(ans)


if __name__ == '__main__':
    main()
