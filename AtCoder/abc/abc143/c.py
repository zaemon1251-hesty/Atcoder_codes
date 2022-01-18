n = int(input())
s = list(input())
ans = n
for i in range(1, n):
    if s[i] == s[i-1]:
        ans -= 1
print(ans)
