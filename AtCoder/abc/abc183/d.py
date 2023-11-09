from itertools import accumulate


def main():
    N, W = map(int, input().split())
    Q = [list(map(int, input().split())) for _ in range(N)]
    T = 2 * 10**5 + 20
    d = [0] * (T)
    for s, t, p in Q:
        d[s] += p
        d[t] -= p
    d = accumulate(d)
    d = list(d)
    # for i in range(T):
    #     print(i, d[i])
    print("Yes" if all(delta <= W for delta in d) else "No")


if __name__ == "__main__":
    main()
