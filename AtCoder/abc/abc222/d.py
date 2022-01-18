mod = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
R = [[0]*3010 for _ in range(N+1)]
R[0][0] = 1
A = [0] + A
B = [0] + B
for i in range(N+1):
    for j in range(3010):
        if A[i] <= j <= B[i] and i > 0:
            R[i][j] = R[i-1][j] + R[i][j-1]
        elif not (i == j == 0):
            R[i][j] = R[i][j-1]
        R[i][j] %= mod
print(R[-1][-1] % mod)
