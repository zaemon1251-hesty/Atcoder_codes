from string import ascii_lowercase


def main():
    P = list(map(int, input().split()))
    alpha = ascii_lowercase
    print("".join(map(lambda x: alpha[x - 1], P)))


if __name__ == '__main__':
    main()
