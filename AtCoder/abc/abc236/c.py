n, m = map(int, input().split())
s = list(map(str, input().split()))
t = set(map(str, input().split()))
ans = []
for i in range(n):
    if s[i] in t:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")
