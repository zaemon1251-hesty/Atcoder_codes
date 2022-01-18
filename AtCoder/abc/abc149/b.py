N, K = map(int, input().split())
r, s, p = map(int, input().split())
ch = {"r": "p", "s": "r", "p": "s"}
point = {"r": r, "s": s, "p": p}
t = list(input())
binds = [[] for _ in range(K)]
for i in range(N):
    binds[i % K].append(ch[t[i]])
ans = 0
for bind in binds:
    pre = -1
    for pt in bind:
        if pt != pre:
            ans += point[pt]
            pre = pt
        else:
            pre = -1
print(ans)
_name__ == '__main__':
# mainc()
maind()
