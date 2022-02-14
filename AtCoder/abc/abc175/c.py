X, K, D = map(int, input().split())
X = abs(X)

if X//D >= K:
    print(X-D*K)
    exit()

K -= X//D
rp = X % D
rm = D - rp

print(rp if K % 2 == 0 else rm)
