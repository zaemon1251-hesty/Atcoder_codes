from collections import defaultdict
from math import gcd


def getPrimeFrac(a, b):
    a //= gcd(a, b)
    b //= gcd(a, b)
    if (a < 0 and b < 0) or (a > 0 and b < 0):
        a *= -1
        b *= -1
    if a == 0:
        b = abs(b)
    return a, b


def fracSame(t1, t2, t3):
    return (t1[0] - t3[0]) * (t2[1] - t3[1]) == (t1[1] - t3[1]) * (t2[0] - t3[0])


def main():
    N, K = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(N)]
    if K == 1:
        print("Infinity")
        exit()
    flag = [[True] * N for _ in range(N)]
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if not flag[i][j]:
                continue
            ii = []
            cnt = 0
            for k in range(N):
                if fracSame(S[i], S[j], S[k]):
                    ii.append(k)
                    cnt += 1
            E = len(ii)
            for u in range(E - 1):
                for v in range(u + 1, E):
                    flag[ii[u]][ii[v]] = False
            ans += 1 if cnt >= K else 0
    print(ans)


if __name__ == "__main__":
    main()
