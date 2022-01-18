G = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = {int(input()) for _ in range(N)}
ans = "No"
for i in range(3):
    if all(G[i][j] in b for j in range(3)):
        ans = "Yes"
    if all(G[j][i] in b for j in range(3)):
        ans = "Yes"
    if all(G[j][j] in b for j in range(3)):
        ans = "Yes"
if all(t in b for t in (G[0][2], G[1][1], G[2][0])):
    ans = "Yes"
print(ans)
