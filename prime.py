def get_prime(n, get_sieve=False):
    prime = [False] * 2 + [True] * (n-2)
    for i in range(2, n):
        if prime[i]:
            for j in range(i*2, n, i):
                prime[j] = False
    if get_sieve:
        return [i for i in range(2, n) if prime[i]]
    else:
        return prime
