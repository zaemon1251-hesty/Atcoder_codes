def main():
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

    T = int(input())
    for _ in range(T):
        N = input()
        yakusu = make_divisors(len(N))
        ans = 10 ** (len(N) - 1) - 1
        for y in yakusu[:-1]:
            na = N[:y]
            tmp = int(na * (len(N) // y))
            if tmp > int(N):
                tmp = int(str(int(na) - 1) * (len(N) // y))
            ans = max(ans, tmp)
        print(ans)


if __name__ == "__main__":
    main()
