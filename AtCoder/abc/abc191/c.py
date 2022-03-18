def main():
    H, W = map(int, input().split())
    A = [list(input())for _ in range(H)]
    ans = 0
    for i in range(H - 1):
        for j in range(W - 1):
            s = 0
            for h in range(2):
                for w in range(2):
                    s += 1 if A[i + h][j + w] == "#" else 0
            ans += 1 if s % 2 != 0 else 0
    print(ans)


if __name__ == '__main__':
    main()
