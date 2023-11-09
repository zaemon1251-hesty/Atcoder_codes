from bisect import bisect_left
from itertools import accumulate


def main():
    N, Q = map(int, input().split())
    A = sorted(map(int, input().split()))
    S = [0] + list(accumulate(A))
    total = S[-1]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        idx = bisect_left(A, x)
        idx = min(N, idx)
        print((2 * idx - N) * x + total - 2 * S[idx])


if __name__ == "__main__":
    main()
