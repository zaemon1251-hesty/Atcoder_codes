def main():
    N = int(input())
    ans = 0
    for i in range(1, pow(10, len(str(N)) // 2 + 1)):
        if int(2 * str(i)) <= N:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
