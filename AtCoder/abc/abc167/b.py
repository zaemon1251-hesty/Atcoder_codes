A, B, C, K = map(int, input().split())
ans = K
if K < A:
    print(ans)
    exit()
K -= A
ans = A
if K < B:
    print(ans)
    exit()
K -= B
print(ans-K)
