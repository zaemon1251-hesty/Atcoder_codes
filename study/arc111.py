def maina():
    n = int(input())
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))
    q = int(input())
    rc = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
    ans = []
    for r, c in rc:
        t1 = min(R[r], C[c])
        t2 = max(R[r], C[c])
        if t1 + t2 > n:
            ans.append("#")
        elif n % 2 != 0 and t1 == t2 == (n + 1)//2:
            ans.append("#")
        else:
            ans.append(".")

    print(*ans, sep="")


def mainb():
    from copy import copy
    n = int(input())
    P = list(map(int, input().split()))
    inf = 1 << 69
    ans = inf

    def same(arr):
        if arr == list(range(n)):
            return 1
        return inf
    for i in range(4):
        rev1 = i >> 1 & 1
        R = copy(P)
        R = R[::-1] if rev1 else R
        i_1 = R.index(1)
        r1 = R[i_1:] + R[:i_1]
        rev2 = i >> 2 & 1
        r1 = r1[::-1] if rev2 else r1
        ans = min(ans, rev1 + rev2 + same(r1) * i_1)
    print(ans)


mainb()
