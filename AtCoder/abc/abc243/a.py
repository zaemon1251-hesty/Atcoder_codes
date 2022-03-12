def main():
    v, a, b, c = map(int, input().split())
    t = [a, b, c]
    s = list("FMT")
    i = 0
    while v >= 0:
        if v < t[i]:
            print(s[i])
            exit()
        v -= t[i]
        i += 1
        i %= 3


if __name__ == '__main__':
    main()
