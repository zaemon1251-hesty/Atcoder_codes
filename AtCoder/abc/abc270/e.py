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

    ok = 0
    ng = 10**12 + 1
    while ng - ok > 1:
        cen = (ok + ng) // 2
        res = 0
        for i in range(N):
            res += min(A[i], cen)
        if res <= K:
            ok = cen
        else:
            ng = cen

    K -= sum(min(A[i], ok) for i in range(N))
    ans = [0] * N
    for i in range(N):
        ans[i] = max(A[i] - ok, 0)
        if K > 0 and ans[i] > 0:
            ans[i] -= 1
            K -= 1

    print(*ans)


if __name__ == "__main__":
    main()
