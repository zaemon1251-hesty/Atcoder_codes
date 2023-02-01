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
    T = input()
    Ns = len(S)
    Nt = len(T)
    res = 0
    ans = []
    for j in range(Nt):
        if T[-1 - j] == S[-1 - j]:
            res += 1
        elif T[-1 - j] == "?" or S[-1 - j] == "?":
            res += 1
    ans.append(res == Nt)

    for i in range(Nt):
        if T[i] == S[(-Nt + i) % Ns]:
            res -= 1
        elif T[i] == "?" or S[(-Nt + i) % Ns] == "?":
            res -= 1

        if T[i] == S[i]:
            res += 1
        elif T[i] == "?" or S[i] == "?":
            res += 1

        ans.append(res == Nt)

    ans = list(map(lambda c: "Yes" if c else "No", ans))

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
