def main():
    X, Y, N = map(int, input().split())
    if Y < 3 * X:
        print(Y * (N // 3) + X * (N % 3))
    else:
        print(X * N)


if __name__ == "__main__":
    main()
