n, k = map(int, input().split())
A = [x for x in map(int, input().split())]
tmp = 0
s = {tmp}
l = [0]
cnt = 0
while True:
    tmp += A[tmp]
    tmp %= n
    if tmp in s:
        break
    l.append(tmp)
    s.add(tmp)
    cnt += 1
    if cnt == k:
        tmp = 0
        ans = 0
        for i in range(k):
            ans += A[tmp]
            tmp += A[tmp]
            tmp %= n
        print(ans)
        exit()
h = l.index(tmp)
d = len(l) - h
ans = 0

# loop
sm = 0
for i in range(d):
    sm += A[tmp]
    tmp += A[tmp]
    tmp %= n
q, r = divmod(k - h, d)
ans += q * sm

# chain
tmp = 0
for i in range(h):
    ans += A[tmp]
    tmp += A[tmp]
    tmp %= n

# tail-chain
tmp = l[h]
for i in range(r):
    ans += A[tmp]
    tmp += A[tmp]
    tmp %= n

print(ans)
