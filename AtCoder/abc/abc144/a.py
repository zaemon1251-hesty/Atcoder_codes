N = int(input())


# 約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors, upper_divisors[::-1]


l, d = make_divisors(N)
ans = N - 1
for ll in l:
    ans = min(ans, ll - 1 + N // ll - 1)
print(ans)
