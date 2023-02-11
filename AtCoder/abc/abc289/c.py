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
    N, M = mi()
    C = []
    A = []

    for i in range(M):
        c = ii()
        cc = li()
        C.append(c)
        A.append(cc)

    ans = 0
    for s in range(1 << M):
        bag = set()
        for i in range(M):
            if s >> i & 1:
                for a in A[i]:
                    bag.add(a)
        if len(bag) == N:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
