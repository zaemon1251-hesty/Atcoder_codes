T = int(input())
ans = []
for _ in range(T):
    a, s = map(int, input().split())
    if s - 2 * a >= 0 and (s - 2 * a & a) == 0:
        ans.append("Yes")
    else:
        ans.append("No")

print(*ans, sep="\n")
