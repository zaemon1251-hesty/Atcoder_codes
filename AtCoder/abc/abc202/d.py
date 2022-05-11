def cmb(n, r):
    r = min(n - r, r)
    a = 1
    b = 1
    for k in range(r):
        a *= (n - r + 1 + k)

        b *= (k + 1)

    return a // b


def gen(A_: int, B_: int, k_: int) -> str:
    if k_ <= 1 or A_ < 1 or B_ < 1:
        return "a" * max(A_, 0) + "b" * max(B_, 0)
    s = cmb(A_ - 1 + B_, A_ - 1)
    if k_ <= s:
        return "a" + gen(A_ - 1, B_, k_)
    else:
        return "b" + gen(A_, B_ - 1, k_ - s)


def main():
    A, B, k = map(int, input().split())
    print(gen(A, B, k))


if __name__ == "__main__":
    main()
