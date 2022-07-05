def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    seen = [False] * N
    X -= 1
    v = X
    while not seen[v]:
        seen[v] = True
        v = A[v] - 1
    print(sum(seen))


if __name__ == '__main__':
    main()
