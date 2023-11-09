from heapq import heappop, heappush

inf = 1 << 60


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = []
    for i, a in enumerate(A):
        S.append((a, i))
    S.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    hp = -inf
    ans = inf
    while S:
        x, i = S.pop()
        if i < K:
            hp = max(hp, i)
        else:
            ans = min(ans, i - hp)
    print(ans if ans < inf else -1)


if __name__ == "__main__":
    main()
