from functools import lru_cache

N, X = map(int, input().split())
A = list(map(int, input().split()))


@lru_cache(maxsize=None)
def dd(x, i):
    if i < N - 1:
        l_coin = (x % A[i + 1]) // A[i]
        m_coin = (A[i + 1] - (x % A[i + 1])) // A[i]
        return min(dd(x + A[i] * m_coin, i + 1) + m_coin, dd(x - A[i] * l_coin, i + 1) + l_coin)
    else:
        return x // A[i]


print(dd(X, 0))
