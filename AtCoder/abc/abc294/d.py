import sys
from heapq import heappush, heappop


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
    patients = [0] * N
    que = list(range(N - 1, -1, -1))
    called = []
    ans = []
    for _ in range(Q):
        q = li()
        if q[0] == 1:
            x = que.pop()
            heappush(called, x)
        if q[0] == 2:
            x = q[1] - 1
            patients[x] = 1
        if q[0] == 3:
            x = heappop(called)
            tmp = []
            while called and patients[x] != 0:
                x = heappop(called)
                tmp.append(x)
            ans.append(x + 1)
            heappush(called, x)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
