import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
now = A
ans = 0

for i in range(32, -1, -1):
    one, zero = [], []

    for x in now:
        if (x >> i) & 1:
            one.append(x)
        else:
            zero.append(x)

    zero.sort(reverse=True)
    lack = max(0, K - len(one))
    cost = 0
    p = pow(2, i)

    for x in zero[:lack]:
        cost += p - x

    nex = []

    if cost <= M:
        M -= cost
        ans += p

        for x in one:
            nex.append(x - p)

        # one で採用されたもののみが，i以下のbitでの走査対象
        # fill された zero の要素は，i未満のbitは全て0だから，i以下のbitでの走査を行っても無視される
        for _ in range(lack):
            nex.append(0)
    else:
        for x in now:
            if (x >> i) & 1:
                nex.append(x - p)
            else:
                nex.append(x)

    now = nex
    assert(len(now) >= K)

print(ans)
