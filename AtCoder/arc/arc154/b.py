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
    S = input()
    T = input()

    if sorted(list(S)) != sorted(list(T)):
        print(-1)
        return

    def check(x):
        ptr = x
        for i in range(N):
            if ptr == N:
                break
            if S[ptr] == T[i]:
                ptr += 1

        return ptr == N

    ok = N
    ng = -1
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen

    print(ok)


if __name__ == "__main__":
    main()
