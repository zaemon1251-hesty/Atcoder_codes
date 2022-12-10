MOD = 10**9+7
N, K = map(int, input().split())
*A, = map(int, input().split())
A.sort(key=lambda x: abs(x), reverse=True)
ans = 1
cntm = 0
for a in A[:K]:
    ans *= a
    ans %= MOD
    if a < 0:
        cntm += 1
if cntm % 2 != 0:
    m1, p1, m2, p2 = MOD, MOD, MOD, MOD
    for a in A[:K]:
        if a < 0:
            m1 = a
        else:
            p2 = a
    for b in A[K:]:
        if p1 == MOD and b >= 0:
            p1 = b
        if m2 == MOD and b <= 0:
            m2 = b
    ok1 = m1 != MOD and p1 != MOD
    ok2 = m2 != MOD and p2 != MOD
    if ok1 and ok2:
        if p1*p2 > m1*m2:
            ans *= p1*pow(m1, MOD-2, MOD)
        else:
            ans *= m2*pow(p2, MOD-2, MOD)
    elif ok1:
        ans *= p1*pow(m1, MOD-2, MOD)
    elif ok2:
        ans *= m2*pow(p2, MOD-2, MOD)
    else:
        A.sort(reverse=True)
        ans = 1
        for a in A[:K]:
            ans *= a
            ans %= MOD
    ans %= MOD

print(ans % MOD)
