from re import L


x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
t = [p, q, r]

s = []
for i in range(3):
    s.extend([[j, i] for j in t[i]])
s.sort(key=lambda x: x[0], reverse=True)
ans = []
cp = 0
cq = 0
i = 0
while len(ans) < x + y:
    d, m = s[i]
    if m == 0 and cp < x:
        cp += 1
        ans.append(d)
    elif m == 1 and cq < y:
        cq += 1
        ans.append(d)
    elif m == 2:
        ans.append(d)
    i += 1
print(sum(ans))
