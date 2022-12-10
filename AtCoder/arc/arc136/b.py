# TODO 未提出

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_Num = [0] * 5010
B_Num = [0] * 5010

for i in range(N):
    A_Num[A[i]] += 1
    B_Num[B[i]] += 1


if A_Num != B_Num:
    print("No")
    exit()

if len(set(A)) != N:
    print("Yes")
    exit()

tA = 0
tB = 0

for i in range(N - 1):
    for j in range(i, N):
        if i == j:
            continue
        if A[i] > A[j]:
            tA += 1
            tA %= 2

        if B[i] > B[j]:
            tB += 1
            tB %= 2

if tA == tB:
    print("Yes")
else:
    print("No")
