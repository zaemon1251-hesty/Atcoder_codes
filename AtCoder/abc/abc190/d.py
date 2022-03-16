def main():
    N = int(input())
    k = 1
    ans = 0
    while k * (k - 1) // 2 <= N:
        s = k * (k - 1) // 2
        r = (N - s) % k
        if r == 0:
            ans += 2 if (N - s) // k > 1 else 1
        k += 1
    print(ans)


if __name__ == '__main__':
    main()
