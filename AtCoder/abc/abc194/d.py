def main():
    N = int(input())
    full = N
    res = 0
    N -= 1
    while N:
        res += full / (full - N)
        N -= 1
    print(res)


if __name__ == '__main__':
    main()
