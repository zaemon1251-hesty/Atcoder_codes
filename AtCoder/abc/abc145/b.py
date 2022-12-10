def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[:N // 2] == S[N // 2:]:
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    main()
