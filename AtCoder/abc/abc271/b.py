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

    N, Q = mi()
    A, L = [], []
    for i in range(N):
        ll, *a = mi()
        L.append(ll)
        A.append(a)

    for _ in range(Q):
        s, t = mi()
        print(A[s - 1][t - 1])


if __name__ == "__main__":
    main()
