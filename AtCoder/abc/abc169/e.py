N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
A = sorted([s[0] for s in S])
B = sorted([s[1] for s in S])
if N % 2 != 0:
    am = A[N//2]
    bm = B[N//2]
    print(bm - am + 1)
else:
    am = A[N//2] + A[N//2 - 1]
    bm = B[N//2] + B[N//2 - 1]
    print(bm - am + 1)
