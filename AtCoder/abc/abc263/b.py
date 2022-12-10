def main():
    N = int(input())
    P = [-1] + list(map(lambda x: int(x) - 1, input().split()))
    cnt = 0
    cr = N - 1
    while cr != 0:
        cr = P[cr]
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
