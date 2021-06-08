def find(G,n,i):
    from collections import deque
    seen = [False]*n
    todo = deque([i])
    while todo:
        idx = todo.popleft()
        seen[idx] = True
        for nx in G[idx]:
            if seen[nx]:continue
            todo.append(nx)
    return sum(seen)


def maina():
    a, b = map(int, input().split())
    if a == b:
        print(a)
    else:
        print(*(set([0,1,2])-set([a, b])))


def mainb():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(max(i - 10, 0)for i in A))

def mainc():
    n, m = map(int, input().split())
    G = [[]for i in range(n)]
    for i in range(m):
        n1, k1 = map(int, input().split())
        G[n1 - 1].append(k1 - 1)

    ans = 0
    for i in range(n):
        ans += find(G,n,i)
    print(ans)



def maind():
    from bisect import bisect_left
    n = int(input())
    t = list(map(int, input().split()))
    inf = 10 ** 5
    s = sum(t)
    s_2 = s / 2

    #dp[i][j]: 料理iまでを使ってj分で完成させることができるかどうか
    dp = [[False] * (inf+1) for _ in range(n+1)]
    dp[0][0] = True
    cnd = []

    for i in range(1, n+1):
        dish = t[i-1]
        for j in range(inf+1):
            #料理iを選ばない場合
            dp[i][j] = dp[i][j] | dp[i-1][j]
            #料理iを選ぶ場合
            if j-dish >= 0:
                dp[i][j] = dp[i][j] | dp[i-1][j-dish]
            if i == n and dp[i][j]:
                cnd.append(j)

    index = bisect_left(cnd, s_2)
    cnd1 = max(cnd[index], s-cnd[index])
    if index + 1 >= len(cnd):
        print(cnd1)
    else:
        cnd2 = max(cnd[index+1], s-cnd[index+1])
        print(min(cnd1, cnd2))


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
