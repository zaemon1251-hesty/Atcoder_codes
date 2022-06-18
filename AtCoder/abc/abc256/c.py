from itertools import product


def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a11, a12, a21, a22 in product(range(1, 31), repeat=4):
        a13 = w1 - a11 - a12
        a23 = w2 - a21 - a22
        a31 = h1 - a11 - a21
        a32 = h2 - a12 - a22
        a33 = w3 - a31 - a32
        if all(i > 0 for i in [a13, a23, a31, a32, a33]) \
                and a13 + a23 + a33 == h3:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
