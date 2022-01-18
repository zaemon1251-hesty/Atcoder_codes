t = list(input())
N = len(t)
ans = 0
for i in range(1 << N):
    a = []
    b = []
    for j in range(N):
        if (i >> j) & 1:
            a.append(int(t[j]))
        else:
            b.append(int(t[j]))
    a = "".join(list(map(str, sorted(a, reverse=True))))
    b = "".join(list(map(str, sorted(b, reverse=True))))
    #print(a, b)
    if a == "" or b == "":
        continue
    ans = max(ans, int(a) * int(b))
print(ans)
c()
