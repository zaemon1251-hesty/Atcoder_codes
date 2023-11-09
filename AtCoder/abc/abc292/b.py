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
    players = [0] * N

    for _ in range(Q):
        c, x = mi()
        x -= 1
        if c == 1:
            players[x] += 1
        elif c == 2:
            players[x] += 2
        else:
            print("Yes" if players[x] >= 2 else "No")


if __name__ == "__main__":
    main()
