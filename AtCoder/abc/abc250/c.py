def main():
    N, Q = map(int, input().split())
    P = range(N)
    P = list(P)
    pos = {p: i for i, p in enumerate(P)}
    X = list(int(input()) for _ in range(Q))
    for x in X:
        x -= 1
        px = pos[x]
        pnx = px + 1
        if px == N - 1:
            pnx = px - 1
        nx = P[pnx]

        P[px], P[pnx] = nx, x
        pos[x], pos[nx] = pnx, px

    for i in range(N):
        P[i] += 1
    print(*P)


if __name__ == '__main__':
    main()
