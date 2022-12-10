N = int(input())
A = list(map(int, input().split()))
A.sort()
inf = 10**18
ans = 1
for i in range(N):
    ans *= A[i]
    if ans > inf:
        print(-1)
        exit()
print(ans)
