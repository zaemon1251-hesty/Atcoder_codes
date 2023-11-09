from bisect import bisect, bisect_left


def main():
    N, M, Q = map(int, input().split())

    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort(key=lambda x: x[1], reverse=True)

    X = list(map(int, input().split()))

    ans = []
    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        available = sorted([*X[:l], *X[r + 1 :]])
        res = 0
        used = set()
        # bug = {}
        for w, v in S:
            idx = bisect_left(available, w)
            flg = False
            while idx < len(available):
                if idx not in used and available[idx] >= w:
                    flg = True
                    break
                idx += 1
            if flg:
                res += v
                used.add(idx)
                # bug[w, v] = [idx, available[idx]]
            # else:
            # bug[w, v] = [idx, None]
        ans.append(res)
        # print(bug)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
