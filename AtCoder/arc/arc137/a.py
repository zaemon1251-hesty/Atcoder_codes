def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    L, R = map(int, input().split())
    w = R - L
    while True:
        for x in range(L, R - w + 1):
            y = x + w
            if gcd(y, x) == 1:
                print(w)
                exit()
        w -= 1


if __name__ == '__main__':
    main()
