N = int(input())
s = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    s.append([a, b])
cand = [s[0][0], s[0][1]]
ans = -1
for i in cand:
    if i == s[1][0] or i == s[1][1]:
        ans = i
if ans == -1:
    print("No")
    exit()
flg = all(ans in i for i in s)
print("Yes" if flg else "No")
