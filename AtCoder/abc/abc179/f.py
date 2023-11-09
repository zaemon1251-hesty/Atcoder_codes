def main():
    N, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    b = [N] * (N + 1)
    a = [N] * (N + 1)
    ans = (N - 2) * (N - 2)
    W, H = N, N
    for q, x in queries:
        if q == 1:
            if x < W:
                for z in range(x, W):
                    b[z] = H
                W = x
            ans -= b[x] - 2
        else:
            if x < H:
                for z in range(x, H):
                    a[z] = W
                H = x
            ans -= a[x] - 2
    print(ans)


if __name__ == "__main__":
    main()
