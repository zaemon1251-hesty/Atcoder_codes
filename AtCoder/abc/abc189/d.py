def main():
    N = int(input())
    S = [input() for _ in range(N)]
    tr, fa = 1, 1
    for s in S:
        if s == "AND":
            fa *= 2
            fa += tr
        else:
            tr *= 2
            tr += fa
    print(tr)


if __name__ == "__main__":
    main()
