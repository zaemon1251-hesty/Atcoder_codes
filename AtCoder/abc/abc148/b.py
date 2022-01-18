N = int(input())
A = list(map(int, input().split()))
sp = 0
for i in range(N):
    if A[i] == sp + 1:
        sp += 1
print(N - sp if sp != 0 else -1)
