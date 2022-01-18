from functools import lru_cache
N = int(input())
K = int(input())
@lru_cache(maxsize=128, typed=False)
def digitDP(n, k):
    if n < 10:
        if k == 0:
            return 1
        elif k == 1:
            return n
        return 0
    else:
        ret = digitDP(n // 10, k)
        if k >= 1:
            ret += digitDP(n // 10, k-1) * (n % 10)
            ret += digitDP(n // 10 - 1, k-1) * (9 - n % 10)
        return ret
print(digitDP(N, K))
_name__ == '__main__':
# maina()
# mainb()
# mainc()
# maind()
maine()
