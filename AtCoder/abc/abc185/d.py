def main():
    def ceil(n, d):
        return (n+d-1)//d
    N, M = map(int, input().split())

    if M == 0:
        print(1)
        exit()

    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N+1]
    M = len(A)

    dist = N
    for i in range(M-1):
        if A[i+1] - A[i] - 1 == 0:
            continue
        dist = min(dist, A[i+1] - A[i] - 1)

    ans = 0
    for i in range(M-1):
        if A[i+1] - A[i] - 1 == 0:
            continue
        ans += ceil(A[i+1] - A[i] - 1, dist)

    print(ans)


if __name__ == '__main__':
    main()
