def main():
    N, M, X, T, D = map(int, input().split())
    U = T - D * X
    print(min(T, U + D * M))


if __name__ == '__main__':
    main()
