A, B, k = map(int, input().split())
S = A + B
ans = ""
for i in range(S):
    if k == 1:
        for _ in range(A):
            ans += "a"
        for _ in range(B):
            ans += "b"
        print(ans)
        exit()
    s = cmb(A - 1 + B, A -1)
    if k <= s:
        ans += "a"
        A -= 1
    else:
        ans += "b"
        B -= 1
        k -= s
print(ans)
bal変数の都合
0
