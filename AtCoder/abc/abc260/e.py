from collections import defaultdict


def main():
    N, M = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(N)]
    inv = defaultdict(list)
    for i, (a, b) in enumerate(C):
        inv[a].append(i)
        inv[b].append(i)

    ans = [0] * (M + 3)

    # (cnt_zero = 0) => 全てのiの条件を満たす
    cnt_zero = N
    cnt = [0] * N
    r = 0
    # 尺取り法
    for l in range(1, M + 1):
        while r <= M and cnt_zero != 0:
            # 区間を広げる処理 (r++)
            # x is an index of the constrains of "r(int)"
            for x in inv[r]:
                if cnt[x] == 0:
                    cnt_zero -= 1
                cnt[x] += 1
            r += 1

        # 条件を満たす区間がない => これから先も条件を満たすことはない
        if cnt_zero != 0:
            break

        # 区間の長さについてインクリメント
        ans[r - l] += 1
        # 区間の長さ制約を満たすためのデクリメント
        ans[M + 1 - l + 1] -= 1

        # 区間を狭める処理 (l++)
        for x in inv[l]:
            cnt[x] -= 1
            if cnt[x] == 0:
                cnt_zero += 1

    for i in range(1, M + 1):
        ans[i] += ans[i - 1]
    print(*ans[1 : M + 1])


if __name__ == "__main__":
    main()
