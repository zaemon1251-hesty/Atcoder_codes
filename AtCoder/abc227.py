def maina():
    n, k, a = map(int, input().split())
    a -= 1
    for i in range(k):
        a += 1
        a %= n
    if a == 0:
        a = n
    print(a)


def mainb():
    N = int(input())
    ans = 0
    A = list(map(int, input().split()))
    for i in range(N):
        flg = False
        for b in range(1, A[i]//3):
            if (A[i] - 3*b) % (4 * b + 3) == 0:
                #print(A[i], b)
                flg = True
                continue
        if not flg:
            ans += 1
    print(ans)


def mainc():
    from math import sqrt, floor
    N = int(input())
    if N == 1:
        print(1)
        exit()
    ans = 0
    for a in range(1, floor(sqrt(N))):
        z = N/a
        #print(a, z)
        for b in range(a, floor(sqrt(z)) + 1):
            ans += floor(z/b) - b + 1
    print(ans)


def maind():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 0, sum(a)//k+1
    while l+1 < r:
        c = (l+r)//2
        s = 0
        for v in a:
            s += min(v, c)
        if s < k*c:
            r = c
        else:
            l = c
    print(l)


if __name__ == '__main__':
    maind()
