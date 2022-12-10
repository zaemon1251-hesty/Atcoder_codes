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

    N, K = mi()
    A = deque(li())
    for i in range(K):
        A.popleft()
        A.append(0)
    print(*list(A))


if __name__ == '__main__':
    main()
