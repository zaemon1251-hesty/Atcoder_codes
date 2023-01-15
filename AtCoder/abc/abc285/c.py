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

    S = input()
    z = 0
    ans = 0
    while len(S) > z:
        ans += pow(26, z)
        z += 1

    res = 0
    for d in range(z):
        res += (ord(S[z - 1 - d]) - ord("A")) * pow(26, d)

    print(ans + res)


if __name__ == '__main__':
    main()
