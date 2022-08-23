from bisect import bisect_left
from itertools import accumulate


def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] + list(accumulate(A))

    if S[-1] < P + Q + R:
        print("No")
        exit()

    for x in range(N - 2):
        y = bisect_left(S, P + S[x])
        if y >= N or S[y] - S[x] != P:
            continue
        z = bisect_left(S, Q + S[y])
        if z >= N or S[z] - S[y] != Q:
            continue
        w = bisect_left(S, R + S[z])
        if w > N or S[w] - S[z] != R:
            continue
        print("Yes")
        exit()

    print("No")


if __name__ == '__main__':
    main()
