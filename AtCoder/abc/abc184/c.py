def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
    elif abs(r1 - r2) + abs(c1 - c2) <= 3 or abs(r1 - r2) == abs(c1 - c2) or abs(r1 + r2) == abs(c1 + c2):
        print(1)
    elif (
        -3 <= abs(r1 - r2) - abs(c1 - c2) <= 3
        or -3 <= abs(r1 + r2) - abs(c1 + c2) <= 3
        or ((c2 - r2) - (c1 - r1)) % 2 == 0
        and ((c2 + r2) - (c1 + r1)) % 2 == 0
    ):
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    main()
