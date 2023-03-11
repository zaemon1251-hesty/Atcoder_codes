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
    A = sorted(set(li()))

    ans = 0
    i = 0
    K = min(K, N, len(A))
    while ans < K:
        if A[i] != ans:
            print(ans)
            return
        i += 1
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
