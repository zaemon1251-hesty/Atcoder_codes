from itertools import combinations


def main():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1].add(v - 1)
        G[v - 1].add(u - 1)

    ans = 0
    for a, b, c in combinations(range(N), 3):
        if b in G[a] and c in G[b] and a in G[c]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
