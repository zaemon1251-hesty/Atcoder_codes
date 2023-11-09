from itertools import product


def main():
    N = int(input())
    G = [[False] * N for _ in range(N)]
    I = sorted(product(range(N), repeat=2), key=lambda x: ((x[0] + x[1]) % 2, x[0], x[1]))
    for v, (i, j) in enumerate(I, 1):
        G[i][j] = v

    for g in G:
        print(*g)


if __name__ == "__main__":
    main()
