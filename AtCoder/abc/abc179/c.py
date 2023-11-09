def main():
    N = int(input())
    ans = 0
    for a in range(1, N + 1):
        ans += N // a
        if N % a == 0:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
