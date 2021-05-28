inf = 10 ** 20
#from collections import deque
def bfs(G, s):
    """
    道と壁があって、上下左右に移動できるグリッドグラフについて、
    スタートからゴールの最小移動回数を求める
    """
    h, w = len(G), len(G[0])
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    dist = [[0]*(w) for i in range(h)]
    d = 1
    seen = [[False]*(w) for i in range(h)]
    seen[s[0]][s[1]] = True
    todo = []
    todo.append(s)
    while todo:
        qq = []
        for x, y in todo:
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                #0-indexで考える
                if nx<0 or nx>=h or ny<0 or ny>=w:
                    continue
                if G[nx][ny] == '#':
                    continue
                if seen[nx][ny]:
                    continue
                seen[nx][ny] = True
                dist[nx][ny] = d
                qq.append((nx,ny))
        todo = qq
        d += 1

    return dist


def maina():
    s = input()
    print(chr(ord(s) + 1))


def mainb():
    n, k, m = map(int, input().split())
    A = list(map(int, input().split()))

    print(m * n - sum(A) if m * n - sum(A) <= k else -1)


def mainc():
    n, m = map(int, input().split())
    p = [0] * n
    ans = 0
    ac = set()
    for i in range(n):
        q, s = map(str, input().split())
        q = int(q) - 1
        if s == "WA":
            p[q] += 1
        elif not q in ac:
            ans += p[q]
    else:
        print(len(ac), ans)


def maind():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = 0

    for i in range(H):
        for j in range(W):
            if G[i][j] == "#":continue
            dists = bfs(G, (i, j))
            dmax = max(max(dist) for dist in dists)
            ans = max(ans, dmax)
    print(ans)



def maine():
    h, n = map(int, input().split())
    A, B = [], []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)



if __name__ == '__main__':
    type
    #maina()
    #mainb()
    #mainc()
    maind()
    #maine()