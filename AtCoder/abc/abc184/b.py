def main():
    N, X = map(int, input().split())
    S = list(input())
    for s in S:
        X += 1 if s == "o" else -1
        X = max(X, 0)
    print(X)


if __name__ == "__main__":
    main()
