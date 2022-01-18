from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cntr = Counter(A)
ans = sum(i * (i - 1) // 2 for i in cntr.values())
for i in range(N):
    n_ans = ans - cntr[A[i]] * (cntr[A[i]] - 1) // 2 + \
        max(0, (cntr[A[i]] - 2) * (cntr[A[i]] - 1) // 2)
    print(n_ans)
