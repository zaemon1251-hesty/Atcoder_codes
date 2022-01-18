n, m = map(int, input().split())
p = [0] * n
ans = 0
ac = set()
for i in range(m):
    q, s = map(str, input().split())
    q = int(q) - 1
    if s == "WA":
        p[q] += 1
    elif not q in ac:
        ac.add(q)
        ans += p[q]
else:
    print(len(ac), ans)
