import sys


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()

    ab = [0] * N
    for k in range(1, N):
        q = make_divisors(k)
        ab[k] = len(q)

    ans = 0
    for k in range(1, N // 2 + 1):
        res = ab[k] * ab[N - k]
        if k != N - k:
            res *= 2
        ans += res

    print(ans)


if __name__ == "__main__":
    main()
