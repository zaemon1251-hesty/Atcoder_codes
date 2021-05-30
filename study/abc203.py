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
    for i in range(n):
        a = list(map(int, input().split()))
        A.append(a)


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
    #maind()
    maine()
    mori = True
