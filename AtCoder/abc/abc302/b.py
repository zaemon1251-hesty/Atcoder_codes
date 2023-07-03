import sys
from itertools import product


def input():
    return sys.stdin.readline().rstrip()


def out(a):
    for arg in a:
        print(*map(lambda x: x + 1, arg))


gold = list("snuke")


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W = mi()
    S = [input() for _ in range(H)]
    for h, w in product(range(H), range(W)):
        row_ids = [[h, w + i] for i in range(5)]
        col_ids = [[h + i, w] for i in range(5)]
        diag_ids = [[h + i, w + i] for i in range(5)]
        diag2_ids = [[h - i, w + i] for i in range(5)]
        if w + 5 <= W and all([S[x][y] == word for (x, y), word in zip(row_ids, gold)]):
            out(row_ids)
            return
        if h + 5 <= H and all([S[x][y] == word for (x, y), word in zip(col_ids, gold)]):
            out(col_ids)
            return
        if w + 5 <= W and h + 5 <= H and all([S[x][y] == word for (x, y), word in zip(diag_ids, gold)]):
            out(diag_ids)
            return
        if w + 5 <= W and h - 4 >= 0 and all([S[x][y] == word for (x, y), word in zip(diag2_ids, gold)]):
            out(diag2_ids)
            return

        if w + 5 <= W and all([S[x][y] == word for (x, y), word in zip(row_ids, gold[::-1])]):
            out(row_ids[::-1])
            return
        if h + 5 <= H and all([S[x][y] == word for (x, y), word in zip(col_ids, gold[::-1])]):
            out(col_ids[::-1])
            return
        if w + 5 <= W and h + 5 <= H and all([S[x][y] == word for (x, y), word in zip(diag_ids, gold[::-1])]):
            out(diag_ids[::-1])
            return
        if w + 5 <= W and h - 4 >= 0 and all([S[x][y] == word for (x, y), word in zip(diag2_ids, gold[::-1])]):
            out(diag2_ids[::-1])
            return

    raise ValueError


if __name__ == "__main__":
    main()
