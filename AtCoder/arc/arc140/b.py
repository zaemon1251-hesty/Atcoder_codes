def main():
    n = int(input())
    s = input()
    xsum, m = 0, 0

    for i in range(1, n - 1):
        if s[i - 1 : i + 2] == "ARC":
            l, r = i - 1, i + 1
            while l - 1 >= 0 and s[l - 1] == "A":
                l -= 1
            while r + 1 < n and s[r + 1] == "C":
                r += 1
            x = min(i - l, r - i)
            xsum += x
            m += 1

    print(min(xsum, m * 2))


if __name__ == "__main__":
    main()
