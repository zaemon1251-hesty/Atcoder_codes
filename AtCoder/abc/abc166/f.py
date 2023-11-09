from functools import lru_cache
import sys

sys.setrecursionlimit(10**7)

N, A_, B_, C_ = map(int, input().split())
CURRENT = {"A": A_, "B": B_, "C": C_}
ans = []
S = [list(input()) for _ in range(N)]


@lru_cache(maxsize=None)
def dfs(t, A=0, B=0, C=0):
    if t == N:
        return True

    dicts = {"A": A, "B": B, "C": C}
    k, l = S[t]

    if dicts[k] == dicts[l] == 0:
        return False

    dicts[k] -= 1
    dicts[l] += 1
    if dicts[k] >= 0 and dfs(t + 1, **dicts):
        ans.append(l)
        return True

    dicts[k] += 2
    dicts[l] -= 2
    if dicts[l] >= 0 and dfs(t + 1, **dicts):
        ans.append(k)
        return True

    return False


dfs(0, **CURRENT)

if len(ans) == 0:
    print("No")
else:
    print("Yes")
    print(*reversed(ans), sep="\n")
