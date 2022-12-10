def main():
    _ = int(input())
    e = []
    for p in [1, 100, 10000]:
        for i in range(1, 100):
            e.append(p * i)
    e.append(10**6)

    print(99 * 3 + 1)
    print(*e, sep="\n")


if __name__ == '__main__':
    main()
