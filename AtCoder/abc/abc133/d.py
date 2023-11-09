def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    flg = 1
    cand = 0
    for i in range(N):
        cand += flg * A[i]
        flg *= -1
    B[0] = cand
    for i in range(1, N):
        tmp = A[i - 1] - B[i - 1] // 2
        B[i] = tmp * 2
    print(*B)


if __name__ == "__main__":
    main()
