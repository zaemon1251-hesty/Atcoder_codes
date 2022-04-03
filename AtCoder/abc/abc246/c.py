def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    for i in range(N):
        p = min(K, A[i] // X)
        A[i] -= p * X
        K -= p
    A.sort(reverse=True)
    for i in range(N):
        p = min(K, (A[i] + X - 1) // X)
        A[i] = max(A[i] - p * X, 0)
        K -= p
    print(sum(A))


if __name__ == '__main__':
    main()
