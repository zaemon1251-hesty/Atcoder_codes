from math import sqrt


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


def main():
    N = int(input())
    ans = 0
    divs = set(make_divisors(N - 1))
    ans += len(divs)

    if N > 2:
        for k in range(2, int(sqrt(N)) + 1):
            D = N
            while D % k == 0:
                D //= k
            if k not in divs and D % k == 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
