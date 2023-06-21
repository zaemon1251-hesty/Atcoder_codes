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
    A = li()
    ans = []
    for i in range(N - 1):
        ans.append(A[i])
        if A[i] < A[i + 1]:
            for aj in range(A[i] + 1, A[i + 1]):
                ans.append(aj)
        else:
            for aj in range(A[i] - 1, A[i + 1], -1):
                ans.append(aj)
    ans.append(A[-1])
    print(*ans)


if __name__ == "__main__":
    main()
