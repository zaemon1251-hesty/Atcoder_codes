def main():
    N = list(input())
    N = map(int, N)
    N = list(N)
    mod3 = [0, 0, 0]
    ans = 0
    for i in N:
        mod3[i % 3] += 1
        ans += i
        ans %= 3

    if ans == 0:
        print(0)
    elif ans == 1:
        if mod3[1] > 0 and len(N) > 1:
            print(1)
        elif mod3[2] > 1 and len(N) > 2:
            print(2)
        else:
            print(-1)
    else:
        if mod3[2] > 0 and len(N) > 1:
            print(1)
        elif mod3[1] > 1 and len(N) > 2:
            print(2)
        else:
            print(-1)


if __name__ == '__main__':
    main()
