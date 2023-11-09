def mov(d, x, y):
    if d == 0:
        return x + 1, y
    elif d == 1:
        return x, y - 1
    elif d == 2:
        return x - 1, y
    else:
        return x, y + 1


def main():
    N = int(input())
    S = input()
    d = 0
    x, y = 0, 0
    for s in S:
        if s == "S":
            x, y = mov(d, x, y)
        else:
            d += 1
            d %= 4
    print(x, y)


if __name__ == "__main__":
    main()
