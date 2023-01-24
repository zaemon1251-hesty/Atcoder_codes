import sys

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
    A, B = list(input()), list(input())

    for i in range(N):
        if int(A[i]) > int(B[i]):
            A[i], B[i] = B[i], A[i]

    A_ = 0
    for i in range(N):
        A_ += int(A[i]) * pow(10, N - i - 1, MOD)
        A_ %= MOD

    ans = 0
    for i in range(N):
        res = A_ * int(B[i])
        res = (res * pow(10, N - i - 1, MOD)) % MOD
        ans += res
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
