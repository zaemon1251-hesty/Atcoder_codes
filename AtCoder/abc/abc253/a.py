def main():
    a, b, c = map(int, input().split())
    print("Yes" if b == sorted([a, b, c])[1] else "No")


if __name__ == '__main__':
    main()
