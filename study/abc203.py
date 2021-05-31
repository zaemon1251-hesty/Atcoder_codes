def one_cumsum(arr):
    """
    [l, r)の区間和が
    f(r) - f(l)　で求められるデータ構造 (0-index)
    """
    from itertools import accumulate

    return [0] + list(accumulate(arr))


def two_cumsum(arr, x):
    """
    [x1,x2) × [y1,y2) の区間和が
    f(x2,y2) - f(x1,y2) - f(x2,y1) + f(x1,y1)　で求められるデータ構造 (0-index)
    """
    s = [[0] * (len(arr[0]) + 1) for _ in range(len(arr) + 1)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + (arr[i][j] > x)
    return s


def check(f, k, n):
    for i in range(k, n + 1):
        for j in range(k, n + 1):
            # [i-k, i) × [j-k, j)
            s = f[i][j] - f[i-k][j] - f[i][j-k] + f[i-k][j-k]
            if int(k**2 / 2) + 1 > s:
                return True
    else:
        return False


def maina():
    a, b, c = map(int, input().split())
    if len(set([a,b,c])) == 3:
        print(0)
        exit()
    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(b)


def mainb():
    n, k = map(int, input().split())
    print(sum(i * 100 * k + k * (k + 1) // 2 for i in range(1, n + 1)))

def mainc():
    n, k = map(int, input().split())
    a=[]
    for i in range(n):
        n1, k1 = map(int, input().split())
        a.append((n1,k1))
    a = sorted(a, key = lambda x:x[0])

    for i in range(n):
        path = a[i][0] - a[i - 1][0] if i >= 1 else a[i][0]
        if k >= path:
            k -= path
            k += a[i][1]
        else:
            print(a[i - 1][0] + k if i >= 1 else k)
            exit()
    else:
        print(min(a[i][0] + k, 10**100))


def maind():
    n, k = map(int, input().split())
    A = []
    ok = 0
    ng = -1
    for _ in range(n):
        a = list(map(int, input().split()))
        ok = max(ok, max(a))
        A.append(a)
    #import numpy as np
    #print(np.array(A))

    while ok - ng > 1:
        #print('--------------------')
        cen = (ok + ng) // 2
        #print(cen)
        f = two_cumsum(A, cen)
        #print(check(f, k, n))
        if check(f, k, n):
            ok = cen
        else:
            ng = cen
    print(ok)


def maine():
    n, m = map(int, input().split())
    x = []
    for i in range(m):
        n1, k1 = map(int, input().split())
        x.append((n1, k1))
    x = sorted(x, key = lambda x:(x[0], x[1]))
    ans = set()
    ans.add(n)
    now = x[0][0]
    black = set()

    for i in range(m):
        xi, yi = x[i]
        if now == xi:
            black.add(yi)
            continue
        else:
            a = set()
            b = set()
            for Y in black:
                if ((Y - 1 in ans) or (Y + 1 in ans)) and (Y not in ans):
                    a.add(Y)
                elif ((Y - 1 not in ans) and (Y + 1 not in ans)) and (Y in ans):
                    b.add(Y)
            for j in a:ans.add(j)
            for j in b:ans.discard(j)
            now = xi
            black = set([yi])

    a = set()
    b = set()
    for Y in black:
        if ((Y - 1 in ans) or (Y + 1 in ans)) and (Y not in ans):
            a.add(Y)
        elif ((Y - 1 not in ans) and (Y + 1 not in ans)) and (Y in ans):
            b.add(Y)
    for j in a:ans.add(j)
    for j in b:ans.discard(j)

    print(len(ans))



if __name__ == '__main__':
    #maina()
    #mainb()
    #mainc()
    maind()
    #maine()
    mori = True
