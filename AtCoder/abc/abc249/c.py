def main():
    N, K = map(int, input().split())
    SS = [set(input()) for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        bg = [0] * 26
        res = 0
        for j in range(N):
            if i >> j & 1:
                for s in SS[j]:
                    t = ord(s) - ord("a")
                    bg[t] += 1
        res = sum(b == K for b in bg)
        ans = max(ans, res)
    print(ans)


if __name__ == '__main__':
    main()
