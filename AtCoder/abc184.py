#半分全列挙
N, T = map(int,input().split())
A = list(map(int,input().split()))
B = A[:N//2]
C = A[N//2:]
D = []
E = []
for i in range(1 << len(B)):
    bag = 0
    for j in range(len(B)):
        if i >> j & 1:
            bag += B[j]
    D.append(bag)

D.sort()
ans = 0
for i in range(1 << len(C)):
    bag = 0
    for j in range(len(C)):
        if i >> j & 1:
            bag += C[j]

    ok = 0
    ng = len(D)
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if bag + D[cen] <= T:
            ok = cen
        else:
            ng = cen
    ans = bag + D[ok] if ans < bag + D[ok] <= T else ans

print(ans)

