def maina():
    a = list(map(int, input().split()))
    print(sum(a) - min(a))


def mainb():
    from math import ceil
    a, b, c, d = map(int, input().split())
    if d * c <= b:
        print(-1)
    else:
        print(ceil(a / (d * c - b)))

def mainc():
    N = int(input())
    C = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            pass
        elif t == 2:
            r -= 0.1
        elif t == 3:
            l += 0.1
        else:
            l += 0.1
            r -= 0.1
        C.append([l,r])

    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            al, ar = C[i]
            bl, br = C[j]
            if al <= br <= ar or bl <= ar <= br:
                ans += 1
    print(ans)


def maind():
    pass


def maine():
    pass

if __name__ =="__main__":
    mori = 20
    #maina()
    #mainb()
    mainc()
    #maind()
    #maine()