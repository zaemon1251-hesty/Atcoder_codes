L, N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(M)]
ans, i, j, p, q = 0, 0, 0, 0, 0
while i < N and j < M:
    if A[i][0] == B[j][0]:
        ans += min(p + A[i][1], q + B[j][1]) - max(p, q)
    if p + A[i][1] < q + B[j][1]:
        p += A[i][1]
        i += 1
    else:
        q += B[j][1]
        j += 1
print(ans)
