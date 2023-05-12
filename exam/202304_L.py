import sys
from typing import List
from collections import deque


def is_united(l: int, row_cutted: List[List[int]], col_cutted: List[List[int]]):
    # (0,0) -> (l,l) がつながっているかどうかチェックする関数
    h, w = l, l

    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    is_row_move = [True, False, False, True]
    dyx_for_edge = [(0, 0), (0, 0), (-1, 0), (0, -1)]

    todo = deque([(0, 0)])
    seen = [[False] * (w + 1) for _ in range(h + 1)]

    while len(todo) > 0:
        y, x = todo.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            edy, edx = dyx_for_edge[i]
            ey, ex = y + edy, x + edx

            # 0-indexで考える
            if nx < 0 or nx >= h + 1 or ny < 0 or ny >= w + 1:
                continue
            if seen[ny][nx]:
                continue

            print(ey, ex, f"({ny}, {nx}) ← ({y}, {x})")

            if is_row_move[i] and row_cutted[ey][ex]:
                print("row cutted")
                continue
            if not is_row_move[i] and col_cutted[ey][ex]:
                print("col cutted")
                continue
            seen[ny][nx] = True
            todo.append((ny, nx))

    return seen[-1][-1]


def main(lines):
    base_infos, cut_lines = lines[0], lines[1:]
    n, l = map(int, base_infos.split())

    # row_cutted[i][j] = 1: i行目の j列目とj+1列目に切れ目がある
    row_cutted = [[0] * (l + 1) for _ in range(l + 1)]
    # col_cutted[i][j] = 1: j列目の i行目とi+1行目に切れ目がある
    col_cutted = [[0] * (l + 1) for _ in range(l + 1)]

    for iter_i in range(n):
        a, b, c, d = map(lambda x: int(x), cut_lines[iter_i].split())

        if a == c:
            if b > d:
                b, d = d, b

            # 端なら切れ目にする
            if b == 0:
                row_cutted[b][a - 1] = 1
                row_cutted[b][a] = 1
            if d == l:
                col_cutted[d][a - 1] = 1
                col_cutted[d][a] = 1

            for i in range(b, d):
                # 列方向の辺削除
                col_cutted[i][a] = 1
                if i < d - 1:
                    # 行方向の辺削除
                    row_cutted[i + 1][a - 1] = 1
                    row_cutted[i + 1][a] = 1
        elif b == d:
            if a > c:
                a, c = c, a

            # 端なら切れ目にする
            if a == 0:
                col_cutted[b - 1][a] = 1
                col_cutted[b][a] = 1
            if c == l:
                col_cutted[b - 1][c] = 1
                col_cutted[b][c] = 1

            for i in range(a, c):
                # 行方向の辺削除
                row_cutted[b][i] = 1
                if i < c - 1:
                    # 列方向の辺削除
                    col_cutted[b - 1][i + 1] = 1
                    col_cutted[b][i + 1] = 1
        else:
            raise RuntimeError("Invalid input")

        print("###################")
        for i in range(l):
            print(*row_cutted[i])
        print("##########")
        for i in range(l):
            print(*col_cutted[i])
        print("###################")

        # チェック
        if not is_united(l, row_cutted, col_cutted):
            print("NO")
            print(iter_i + 1)
            return

    print("YES")


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
