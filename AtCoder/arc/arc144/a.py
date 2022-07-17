def main():
    N = int(input())
    M = 2 * N
    print(M)
    x2 = []
    while N:
        for i in range(4, -1, -1):
            if N >= i:
                N -= i
                x2.append(str(i))
                break
    bigint = int("".join(reversed(x2)))
    print(bigint)


if __name__ == '__main__':
    main()
