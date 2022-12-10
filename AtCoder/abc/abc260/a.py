from collections import Counter


def main():
    A = list(input())
    s = Counter(A)
    for ss, c in s.items():
        if c==1:
            print(ss)
            exit()
    else:
        print(-1)


if __name__ == '__main__':
    main()
