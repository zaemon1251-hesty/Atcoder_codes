from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)


def get_new_g(g, *args):
    ng = list(g)
    for i in args:
        ng[i] = "1"
    return "".join(ng)


def main():
    H, W, A, B = map(int, input().split())

    used = [[False] * W for _ in range(H)]

    def dfs(r, c, a, b):
        if a < 0 or b < 0:
            return 0
        if c == W:
            r += 1
            c = 0
        if r == H:
            return 1
        if used[r][c]:
            return dfs(r, c + 1, a, b)

        res = 0
        # 1x1 をおく
        used[r][c] = True
        res += dfs(r, c + 1, a, b - 1)

        # 1x2 をおく
        if c + 1 < W and not used[r][c + 1]:
            used[r][c + 1] = True
            res += dfs(r, c + 1, a - 1, b)
            used[r][c + 1] = False

        # 2x1 をおく
        if r + 1 < H and not used[r + 1][c]:
            used[r + 1][c] = True
            res += dfs(r, c + 1, a - 1, b)
            used[r + 1][c] = False

        used[r][c] = False
        return res

    ans = dfs(0, 0, A, B)
    print(ans)


if __name__ == "__main__":
    main()
