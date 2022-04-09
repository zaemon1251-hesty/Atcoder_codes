from itertools import accumulate


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cur, mx, mn, x, y = 0, 0, 0, 0, 0
    for a in A:
        cur += 1 if a == 1 else -1
        x = min(x, cur - mx)
        y = max(y, cur - mn)
        mx = max(mx, cur)
        mn = min(mn, cur)
    print(y - x + 1)


if __name__ == '__main__':
    main()
