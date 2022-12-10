def simple(x, n):
    return all(x[i] <= x[i + 1] for i in range(n - 1))


def main():
    N = int(input())
    A = list(map(int, input().split()))
    if simple(A, N):
        print("YES")
        exit()
    for i in range(N - 1):
        for j in range(i + 1, N):
            A[i], A[j] = A[j], A[i]
            if simple(A, N):
                print("YES")
                exit()
            A[i], A[j] = A[j], A[i]
    print("NO")


if __name__ == '__main__':
    main()
