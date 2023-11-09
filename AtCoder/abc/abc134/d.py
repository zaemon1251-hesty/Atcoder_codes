def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N, 0, -1):
        other = 0
        for j in range(2 * i, N + 1, i):
            other += B[j]
        if A[i - 1] == other % 2:
            B[i] = 0
        else:
            B[i] = 1
    print(sum(B))
    ans = [i for i in range(N + 1) if B[i] == 1]
    if ans:
        print(*ans)


if __name__ == "__main__":
    main()
