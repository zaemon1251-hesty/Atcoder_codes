from math import inf


def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    ans = inf

    used = 0
    for i, (a, b) in enumerate(A):
        ans = min(ans, used + a + max(0, X - i) * b)
        used += a + b
    print(ans)


if __name__ == '__main__':
    main()
