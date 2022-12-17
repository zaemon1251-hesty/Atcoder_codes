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
    S = list(input())
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        else:
            if cnt % 2 == 0 and S[i] == ",":
                S[i] = "."
    print(''.join(S))


if __name__ == '__main__':
    main()
