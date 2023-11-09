# 素数列挙
def get_prime(n, get_sieve=False):
    prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if prime[i]:
            for j in range(i * 2, n, i):
                prime[j] = False
    if get_sieve:
        return [i for i in range(2, n) if prime[i]]
    else:
        return prime


def main():
    primes = get_prime(210)
    A, B, C, D = map(int, input().split())
    for tak in range(A, B + 1):
        flg = False
        for ao in range(C, D + 1):
            if primes[tak + ao]:
                flg = True
                break
        if not flg:
            print("Takahashi")
            exit()
    print("Aoki")


if __name__ == "__main__":
    main()
