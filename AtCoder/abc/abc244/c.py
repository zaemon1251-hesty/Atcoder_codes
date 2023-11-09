def main():
    N = int(input())
    p = [False] * (2 * N + 2)
    p[0] = True
    s = 0
    while True:
        if s == 1:
            i = int(input())
            if i == 0:
                exit()
            p[i] = True
        else:
            i = p.index(False)
            print(i)
            p[i] = True
        s = 1 - s


if __name__ == "__main__":
    main()
