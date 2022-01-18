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
