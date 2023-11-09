def main():
    A, B, C = map(int, input().split())
    A, B, C = sorted([A, B, C])
    if C >= 2 * C - A - B:
        print(C)
    else:
        print(-1)


if __name__ == "__main__":
    main()
