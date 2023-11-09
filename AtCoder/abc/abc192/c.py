import sndhdr


def main():
    N, K = map(int, input().split())
    for _ in range(K):
        s = sorted(list(str(N)))
        _min = int("".join(s))
        _max = int("".join(s[::-1]))
        N = _max - _min
    print(N)


if __name__ == "__main__":
    main()
