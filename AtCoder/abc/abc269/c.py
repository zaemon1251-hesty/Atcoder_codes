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
    bitset = []
    for i in range(60):
        if (N >> i) & 1:
            bitset.append(i)

    B = len(bitset)
    for i in range(1 << B):
        res = 0
        for j in range(B):
            if i >> j & 1:
                res |= 1 << bitset[j]
        print(res)


if __name__ == "__main__":
    main()
