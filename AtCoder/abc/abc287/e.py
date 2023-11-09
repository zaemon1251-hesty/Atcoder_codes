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

    N = ii()
    S = sorted([(input(), i) for i in range(N)])
    ans = [0] * N
    for i in range(N):
        si = S[i][0]
        idx = S[i][1]

        res1 = 0
        if i > 0:
            sj = S[i - 1][0]
            while len(si) > res1 and len(sj) > res1 and si[res1] == sj[res1]:
                res1 += 1

        res2 = 0
        if i < N - 1:
            sj = S[i + 1][0]
            while len(si) > res2 and len(sj) > res2 and si[res2] == sj[res2]:
                res2 += 1

        ans[idx] = max(res1, res2)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
