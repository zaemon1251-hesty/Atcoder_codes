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
    S = input()
    T = input()
    diff = sum(s != t for s, t in zip(S, T))
    if diff % 2 == 1:
        print(-1)
        exit()

    ans = []
    dist_ST = 0
    for i in range(N):
        if S[i] == T[i]:
            ans.append(0)
            continue

        if S[i] == "1" and dist_ST >= diff:
            ans.append(1)
            dist_ST -= 1
        elif T[i] == "1" and -dist_ST >= diff:
            ans.append(1)
            dist_ST += 1
        else:
            ans.append(0)
            dist_ST += 1 if S[i] == "1" else -1
        diff -= 1

    print("".join(map(str, ans)))


if __name__ == '__main__':
    main()
