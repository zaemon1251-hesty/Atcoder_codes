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
    A = li()
    A = list(map(lambda x: x - 1, A))
    C0 = list(range(N))

    for a in A:
        C0[a], C0[a + 1] = C0[a + 1], C0[a]

    pos = {c: i for i, c in enumerate(C0, 1)}

    C = list(range(N))
    for a in A:
        if C[a] == 0:
            print(pos[C[a + 1]])
        elif C[a + 1] == 0:
            print(pos[C[a]])
        else:
            print(pos[0])
        C[a], C[a + 1] = C[a + 1], C[a]


if __name__ == '__main__':
    main()
