def main():
    N, K = map(int, input().split())
    SS = [input() for _ in range(N)]
    ans = [0] * 26
    for i in range(1 << N):
        bg = [0] * 26
        for j in range(N):
            if i >> j & 1:
                for s in set(SS[j]):
                    t = ord(s) - ord("a")
                    bg[t] += 1
        for alb in range(26):
            if bg[alb] == K:
                ans[alb] = 1
    print(sum(ans))


if __name__ == '__main__':
    main()
