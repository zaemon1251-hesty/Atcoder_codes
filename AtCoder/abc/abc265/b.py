def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    Z = [list(map(int, input().split())) for _ in range(M)]

    i = 0
    bonus_i = 0
    dep = T
    while i < N - 1 and dep > 0:
        if bonus_i < M and i == Z[bonus_i][0] - 1:
            dep += Z[bonus_i][1]
            bonus_i += 1
        dep -= A[i]
        i += 1

    if i == N - 1 and dep > 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
