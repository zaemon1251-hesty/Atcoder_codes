def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    M = 200100
    cnt = [0] * M
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, M):
        for j in range(1, M):
            k = i * j
            if k < M:
                ans += cnt[i] * cnt[j] * cnt[k]
            else:
                break
    print(ans)


if __name__ == "__main__":
    main()
