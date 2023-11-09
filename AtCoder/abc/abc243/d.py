def main():
    N, X = map(int, input().split())
    t = list(bin(X))
    S = list(input())
    for s in S:
        if s == "U" and len(t) > 1:
            t.pop()
        if s == "L":
            t.append("0")
        if s == "R":
            t.append("1")
    ans = 0
    i = 1
    while t:
        s = t.pop()
        if s == "b":
            break
        ans += i * int(s)
        i *= 2
    print(int(ans))


if __name__ == "__main__":
    main()
