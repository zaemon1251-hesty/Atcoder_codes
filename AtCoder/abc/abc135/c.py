def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N == 1:
        print(min(B[0], A[0] + A[1]))
        exit()
    ans = 0
    for i in range(N):
        mon_i_num = min(A[i], B[i])
        ans += mon_i_num
        A[i] -= mon_i_num
        B[i] -= mon_i_num

        mon_i_1_num = min(A[i + 1], B[i])
        ans += mon_i_1_num
        A[i + 1] -= mon_i_1_num
        B[i] -= mon_i_1_num
    print(ans)


if __name__ == "__main__":
    main()
