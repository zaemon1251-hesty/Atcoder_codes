def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                v1, v2 = A[i][0] - A[j][0], A[i][1] - A[j][1]
                u1, u2 = A[k][0] - A[j][0], A[k][1] - A[j][1]
                if v1 * u2 - v2 * u1 == 0:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
