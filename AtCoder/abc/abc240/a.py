def main():
    a, b = map(int, input().split())
    a %= 10
    b %= 10
    print("Yes" if abs(a-b) == 1 or abs(a-b) == 9 else "No")


if __name__ == '__main__':
    main()
