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
    A = list(mi())

    def dfs(d, B):
        if d == -1:
            return 0

        S, T = [], []
        for b in B:
            if (b >> d) & 1:
                T.append(b)
            else:
                S.append(b)

        if not S:
            return dfs(d - 1, T)

        if not T:
            return dfs(d - 1, S)

        return min(dfs(d - 1, S), dfs(d - 1, T)) | 1 << d

    print(dfs(29, A))


if __name__ == "__main__":
    main()
