def main():
    N, M, T = map(int, input().split())
    lim = N
    A = [list(map(int, input().split())) for _ in range(M)]
    now = 0
    for i in range(M):
        a, b = A[i]
        N -= a - now
        if N <= 0:
            print("No")
            exit()
        N += b - a
        N = min(N, lim)
        now = b
    N -= T - now
    if N <= 0:
        print("No")
        exit()
    print("Yes")


if __name__ == "__main__":
    main()
