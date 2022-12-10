def main():
    A, B, C = map(int, input().split())
    print(C - min(A - B, C))


if __name__ == '__main__':
    main()
