def make_divisors(n):
    # 約数列挙

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
    print(*make_divisors(N), sep="\n")


if __name__ == "__main__":
    main()
