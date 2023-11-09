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

    S = [input() for _ in range(10)]

    for a in range(10):
        for c in range(10):
            if S[a][c] == "#":
                break
        else:
            continue
        break

    for b in range(10)[::-1]:
        for d in range(10)[::-1]:
            if S[b][d] == "#":
                break
        else:
            continue
        break

    print(a + 1, b + 1)
    print(c + 1, d + 1)


if __name__ == "__main__":
    main()
