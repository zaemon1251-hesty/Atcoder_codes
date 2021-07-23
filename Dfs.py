# ABC 138-D
# 深さ優先探索　
import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

'''
#dfsのひな型
seen=[False]*n

def dfs(G,v):
    seen[v]=True

    for next_v in G[v]:
        if seen[next_v]=True:continue
        dfs(G,next_v)
'''
# 木のひな型

# 根の深さ
depth = [0]*n
# 部分木の大きさ
subtree = [0]*n
# この問題特有の設定
counter = [0]*n


def dfs(G, v, p, d, x):
    depth[v] = d
    counter[v] += x
    for next_v in G[v]:
        if next_v == p:
            continue
        dfs(G, next_v, v, d+1, counter[v])
    '''
    subtree[v]=1
    for c in G[v]:
        subtree[v]+=subtree[c]
	'''


G = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

for j in range(m):
    p, x = map(int, input().split())
    p -= 1
    counter[p] += x

# v[0]を根とする
root = 0
# 探索(-1はv[0]の親がいないことを表す）
dfs(G, root, -1, 0, 0)

print(*counter, sep=' ')


# 行きがけ、帰りがけに使う変数
now = 0


def in_out(G, n):
    from sys import setrecursionlimit
    setrecursionlimit(10**6)
    seen = [False] * n
    before = [0] * n
    after = [0] * n

    def dfs(v):
        global now
        seen[v] = True
        before[v] = now
        now += 1
        for next_v in G[v]:
            if seen[next_v] == True:
                continue
            dfs(next_v)
        after[v] = now
        now += 1
    # global変数の初期化
    global now
    now = 0
    return before, after
