N = int(input())
*L, = map(int, input().split())
ans = set()
L.sort()
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if L[i] == L[j] or L[k] == L[j] or L[k] == L[i]:
                continue
            if L[j] - L[i] < L[k] < L[j] + L[i]:
                ans.add((i, j, k))
print(len(ans))
