def main():
    N = int(input())
    T = list(map(int, input().split()))
    ans = 0
    for i, t in enumerate(T):
        y = (ans // (1 << t) + 1) * (1 << t)
        if y % (1 << (t + 1)) == 0:
            y += 1 << t
        ans = y
    print(ans)


if __name__ == "__main__":
    main()
