def main():
    N, X = map(int, input().split())
    X -= 1
    p = X // N
    print(chr(p + ord("A")))


if __name__ == '__main__':
    main()
