N = int(input())
ans = 0
A = list(map(int, input().split()))
for i in range(N):
    flg = False
    for b in range(1, A[i]//3):
        if (A[i] - 3*b) % (4 * b + 3) == 0:
            #print(A[i], b)
            flg = True
            continue
    if not flg:
        ans += 1
print(ans)
