N, D = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x: (x[1]))
removed = -1
ans = 0
for a, b in S:
    # a が removed より大きい = まだ取り除いてない
    if a > removed:
        removed = b + D - 1
        ans += 1
print(ans)
