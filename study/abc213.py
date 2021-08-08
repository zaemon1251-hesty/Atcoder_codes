import sys


def maina():
    n = int(input())


a = list(map(int, input().split()))
b = sorted(a)
for i in range(n):
    if a[i] == b[-2]:
        print(i + 1)
        exit()


def mainb():
    n = int(input())


a = list(map(int, input().split()))
a = sorted(a)
print(a[1])


def mainc():


h, w, n = map(int, input().split())
x = []
y = []
z = []
for i in range(n):
    a, b = map(int, input().split())
    x.append([a, i])
    y.append([b, i])
    z.append([a, b])

ans = [[-1, -1] for _ in range(n)]
x.sort(key=lambda x: x[0])
y.sort(key=lambda x: x[0])
cntx = 1
cnty = 1
px = x[0][0]
py = y[0][0]
for j in range(n):
    xx, s = x[j]
    yy, t = y[j]
    if xx > px:
        cntx += 1
        px = xx
    if yy > py:
        cnty += 1
        py = yy
    ans[s][0] = cntx
    ans[t][1] = cnty

for item in ans:
    print(item[0], item[1])


def maind():


sys.setrecursionlimit(10**6)

n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [False]*n
ans = []
fl = False


def dfs(G, v):
    global ans
    global fl
    if v == 0 and fl:
        return
    seen[v] = True
    ans.append(v + 1)

    for next_v in sorted(G[v]):
        if seen[next_v] == True:
            continue
        dfs(G, next_v)
        if ans[-1] != v + 1:
            ans.append(v + 1)
        fl = True

    if ans[-1] != v + 1:
        ans.append(v + 1)


dfs(G, 0)
print(*ans, sep=" ")


def maine():
    from math import gcd
    N, M = map(int, input().split())
    D = []
    for i in range(M):
        a, c = map(int, input().split())
        D.append((a, c))
    D.sort(key=lambda x: x[1])

    ans = 0
    X = N
    #sdgs = N
    for i in range(M):
        a, c = D[i][0], D[i][1]
        tmp = gcd(X, a)
        ans += c * (X - tmp)
        X = tmp

    print(ans if X == 1 else -1)


if __name__ == "__main__":
    mori = 21
    # maina()
    # mainb()
    # mainc()
    # maind()
    # maine()
    # mainf()
