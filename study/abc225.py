def maina():
    # map(int, input().split())
    s = list(input())
    ans = 1
    if len(set(s)) == 3:
        ans = 6
    elif len(set(s)) == 2:
        ans = 3
    else:
        ans = 1
    print(ans)


def mainb():
    N = int(input())
    s = []
    for _ in range(N-1):

        a, b = map(int, input().split())
        s.append([a, b])
    cand = [s[0][0], s[0][1]]
    ans = -1
    for i in cand:
        if i == s[1][0] or i == s[1][1]:
            ans = i
    if ans == -1:
        print("No")
        exit()
    flg = all(ans in i for i in s)
    print("Yes" if flg else "No")


def mainc():
    ok = True
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]

    def dev(n):
        if n % 7 == 0:
            return 7
        else:
            return n % 7

    for i in range(n):
        for j in range(1, m):
            if dev(B[i][j]) - dev(B[i][j-1]) != 1:
                ok = False

    for j in range(m):
        for i in range(1, n):
            if B[i][j] - B[i-1][j] != 7:
                ok = False

    print('Yes' if ok else 'No')
    return 0


def maind():
    from collections import deque
    N, Q = map(int, input().split())
    par = [-1] * N
    ch = [-1] * N
    A = []
    for i in range(Q):
        t = input().split()
        if t[0] == "1":
            x, y = int(t[1])-1, int(t[2]) - 1
            ch[x] = y
            par[y] = x
        elif t[0] == "2":
            x, y = int(t[1]) - 1, int(t[2]) - 1
            ch[x] = -1
            par[y] = -1
        else:
            x = int(t[1]) - 1
            ans = deque([x + 1])
            z = par[x]
            while z != -1:
                ans.appendleft(z + 1)
                z = par[z]
            w = ch[x]
            while w != -1:
                ans.append(w + 1)
                w = ch[w]
            ans.appendleft(len(ans))
            A.append(" ".join(list(map(str, ans))))
    print()
    print(*A, sep="\n")


def maine():
    # 区間スケジューリング問題

    from functools import cmp_to_key
    inf = 1 << 60

    def leftIsBigger(l, r):
        return l[0] * r[1] >= r[0] * l[1]

    def compare(x, y):
        print(x, y)
        return not leftIsBigger(x[1], y[1])
    N = int(input())
    S = []
    for i in range(N):
        x, y = map(int, input().split())
        A = [(y-1, x), (y, x-1)]
        S.append(A)
    S.sort(key=cmp_to_key(compare))
    rmax = (0, 1)
    ans = 0
    for item in S:
        A = item
        if leftIsBigger(A[0], rmax):
            rmax = A[1]
            ans += 1
    print(ans)


maine()
