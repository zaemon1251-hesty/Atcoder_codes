# map(int, input().split())
s = list(input())
ans = 1
if len(set(s)) == 3:
    ans = 6
elif len(set(s)) == 2:
    ans = 3
else:
    ans = 1
print(ans)
