from math import inf


def get_dist(x, y):
    print(f"? {x} {y}")
    d = int(input())
    if d < 0:
        exit()
    return d


def main():
    N = int(input())
    anses = [inf, inf]
    for i in range(3, N + 1):
        d1 = get_dist(1, i)
        d2 = get_dist(2, i)
        anses.append(d1 + d2)

    ans = min(anses)

    if ans == 3:
        threes = [i + 1 for i, v in enumerate(anses) if v == 3]
        if len(threes) == 2:
            x, y = threes
            dxy = get_dist(x, y)
            ans = 1 if dxy != 1 else 3
        else:
            ans = 1

    print(f"! {ans}")


if __name__ == "__main__":
    main()
