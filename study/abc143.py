def maina():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))


def mainb():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)


def mainc():
    n = int(input())
    s = list(input())
    ans = n
    for i in range(1, n):
        if s[i] == s[i-1]:
            ans -= 1
    print(ans)


def maind():
    from bisect import bisect_left, bisect
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            w = abs(d[i]-d[j])
            m = d[i] + d[j]
            l = bisect(d[j + 1:], w)
            r = bisect_left(d[j + 1:], m)
            # print(d[i], d[j], d[j + 1:])
            ans += max(0, r - l)
    print(ans)


maind()
