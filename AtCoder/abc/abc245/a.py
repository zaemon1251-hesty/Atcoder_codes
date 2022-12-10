a, b, c, d = map(int, input().split())


def time(h, m, s):
    return 3600 * h + 60 * m + s


print("Aoki" if time(a, b, 0) >= time(c, d, 1) else "Takahashi")
