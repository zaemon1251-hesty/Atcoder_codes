def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    _min = min(min(A[i]) for i in range(H))
    ans = 0
    for h in range(H):
        for w in range(W):
            ans += A[h][w] - _min
    print(ans)


if __name__ == "__main__":
    main()
