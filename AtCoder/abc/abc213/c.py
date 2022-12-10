# 座標圧縮
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
