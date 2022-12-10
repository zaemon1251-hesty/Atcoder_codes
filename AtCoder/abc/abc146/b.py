def main():
    N = int(input())
    S = input()
    st = ord("A")
    print("".join(map(lambda x: chr(st + (ord(x) - st + N) % 26), S)))


if __name__ == '__main__':
    main()
