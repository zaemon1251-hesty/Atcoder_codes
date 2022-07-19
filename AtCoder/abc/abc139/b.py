def main():
    A, B = map(int, input().split())
    tap = A
    cnt = 1
    if B == 1:
        print(0)
    else:
        while tap < B:
            tap += A - 1
            cnt += 1
        print(cnt)


if __name__ == '__main__':
    main()
