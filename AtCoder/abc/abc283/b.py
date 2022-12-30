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

    _ = ii()
    A = li()
    Q = ii()
    for _ in range(Q):
        t = li()
        if t[0] == 1:
            k, x = t[1:]
            k -= 1
            A[k] = x
        else:
            k = t[1]
            k -= 1
            print(A[k])


if __name__ == '__main__':
    main()
