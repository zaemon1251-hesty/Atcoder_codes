from bisect import bisect

N = int(input())
A = [float("inf")] * N
A[-1] = 0
for i in range(N):
    A[i] = A[i - 1] + i + 1
B = []
while N > 0:
    idx = bisect(A, N)
    N -= A[idx - 1]
    B.append(idx)
M = len(B) - 1
if M == 0:
    exit(print("7" * B[0]))
C = [1, 2, 3, 4, 5, 6, 8, 9]


def dfs(idx=1, pre=[]):
    if len(pre) == 2 * M + 1:
        exit(print("".join(pre)))
    for c in C:
        fit = True
        for i in range(len(pre)):
            a = "".join(pre[i:]) + str(c)
            if int(a) % 7 == 0:
                fit = False
                break
        if fit:
            dfs(idx + 1, pre + [str(c), "7" * B[idx]])


dfs(1, ["7" * B[0]])
c()
