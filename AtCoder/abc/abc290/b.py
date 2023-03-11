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
    S = list(input())
    ans = []
    cnt = 0
    for i in range(N):
        if S[i] == "o" and cnt < K:
            ans.append("o")
            cnt += 1
        else:
            ans.append("x")
    print("".join(ans))


if __name__ == '__main__':
    main()
