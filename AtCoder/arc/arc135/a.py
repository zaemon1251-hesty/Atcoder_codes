from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
MOD = 998244353
X = int(input())

ans = 1


@lru_cache(maxsize=None)
def dfs(x):
    if x <= 3:
        return x
    return dfs((x+1)//2) * dfs(x//2) % MOD


ans = dfs(X)

print(ans % MOD)
