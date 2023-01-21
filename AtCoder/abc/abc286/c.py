import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    N, A, B = mi()
    S = deque(list(input()))
    ans = 1 << 60
    for i in range(N):
        res = i * A
        for k in range(N // 2):
            if S[k] != S[-1 - k]:
                res += B
        ans = min(ans, res)
        S.append(S.popleft())
    print(ans)


if __name__ == '__main__':
    main()
