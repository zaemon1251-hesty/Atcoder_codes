N, D = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
ans = sum(x**2 + y**2 <= D**2 for x, y in S)
print(ans)
