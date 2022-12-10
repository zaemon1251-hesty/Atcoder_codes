from itertools import permutations
N, M = map(int, input().split())
T = [tuple(map(lambda x:int(x) - 1, input().split())) for _ in range(M)]
A = set(tuple(map(lambda x: int(x) - 1, input().split()))
        for _ in range(M))
for P in permutations(range(N), N):
    flg = True
    for i, j in T:
        mi = min(P[i], P[j])
        Mj = max(P[i], P[j])
        if not (mi, Mj) in A:
            flg = False
            break
    if flg:
        print("Yes")
        return
print("No")
