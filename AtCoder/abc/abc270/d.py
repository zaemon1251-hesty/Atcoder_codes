import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()
    A = li()

    # turn = 0
    # while N >= A[0]:
    #     idx = bisect_left(A, N)
    #     if idx == K or A[idx] > N:
    #         idx -= 1
    #     scores[turn] += A[idx]
    #     N -= A[idx]
    #     turn = 1 - turn
    # print(scores[0])

    dp = [0] * (N + 1)
    for i in range(N + 1):
        for k in range(K):
            if i < A[k]:
                continue
            dp[i] = max(dp[i], i - dp[i - A[k]])
    print(dp[N])


if __name__ == '__main__':
    main()
