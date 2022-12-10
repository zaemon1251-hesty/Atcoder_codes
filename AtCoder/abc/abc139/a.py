def main():
    S = input()
    T = input()
    print(sum(s == t for s, t in zip(S, T)))


if __name__ == '__main__':
    main()
