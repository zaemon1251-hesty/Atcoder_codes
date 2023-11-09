from functools import lru_cache


def main():
    S = list(input())
    N = len(S)
    Q = int(input())
    A = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    E = list("ABC")

    @lru_cache(None)
    def f(s, k):
        if s == 0:
            return S[k]
        elif k == 0:
            idx = E.index(S[0])
            return E[(idx + s) % 3]
        elif k % 2 == 0:
            idx = E.index(f(s - 1, k // 2))
            return E[(idx + 1) % 3]
        else:
            idx = E.index(f(s - 1, k // 2))
            return E[(idx + 2) % 3]

    for s, k in A:
        ans.append(f(s, k - 1))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
