from functools import lru_cache


@lru_cache(None)
def f(mask, last):
    for i in range(n):
        if not (mask & (1 << i)) and ll[i][0] == last and not f(
                mask | (1 << i), ll[i][1]):
            return True
    return False


n = int(input())
ll = [input() for _ in range(n)]
L = [(ord(s[0]), ord(s[-1])) for s in ll]
print("First" if any(not f(1 << i, L[i][1]) for i in range(n)) else "Second")
