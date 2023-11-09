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
    A = sorted(li(), reverse=True)
    cur = 0
    ans = [0] * N
    used = set()
    for i in range(N):
        if i < N - 1 and A[i] == A[i + 1]:
            cur += 1
        else:
            cur += 1
            ans[len(used)] = cur
            cur = 0
            used.add(A[i])
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
