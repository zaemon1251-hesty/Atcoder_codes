from collections import defaultdict

inf = 1 << 60


def main():
    N = int(input())
    cols = defaultdict(list)
    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort(key=lambda x: x[0])

    cols[0].append(0)
    for x, c in S:
        cols[c].append(x)
    cols[N + 1].append(0)

    ans_l, ans_r = 0, 0
    keys = sorted(cols.keys())
    for i, k in enumerate(keys[1:], start=1):
        prev_k = keys[i - 1]

        diff_l = min(
            abs(cols[k][-1] - cols[prev_k][0]) + ans_l,
            abs(cols[k][-1] - cols[prev_k][-1]) + ans_r
        )
        diff_r = min(
            abs(cols[k][0] - cols[prev_k][0]) + ans_l,
            abs(cols[k][0] - cols[prev_k][-1]) + ans_r
        )

        dist = abs(cols[k][-1] - cols[k][0])
        ans_l = diff_l + dist
        ans_r = diff_r + dist

    print(min(ans_r, ans_l))


if __name__ == '__main__':
    main()
