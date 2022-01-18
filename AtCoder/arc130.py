def maina():
    N = int(input())
    S = list(input())
    t = []
    cont = 1
    ans = 0
    for i in range(1, N):
        if S[i] == S[i-1]:
            cont += 1
        else:
            ans += cont * (cont - 1) // 2
            cont = 1
    else:
        ans += cont * (cont - 1) // 2
    print(ans)


def mainb():
    H, W, C, Q = map(int, input().split())

    C = [0] * C
    query = []
    for i in range(Q):
        t, n, c = map(int, input().split())
        query.append([t, n, c])
    col = 0
    row = 0
    used_col = set()
    used_row = set()
    # c_row_cnt = [set()] * len(C)
    # c_col_cnt = [set()] * len(C)
    for t, n, c in query[::-1]:
        n -= 1
        c -= 1
        if t == 2 and n not in used_col:
            used_col.add(n)
            C[c] += H
            C[c] -= row
            #C[c] += len(c_row_cnt[c])
            # c_col_cnt[c].add(n)
            col += 1
        elif t == 1 and n not in used_row:
            used_row.add(n)
            C[c] += W
            C[c] -= col
            #C[c] += len(c_col_cnt[c])
            # c_row_cnt[c].add(n)
            row += 1
        # print(*C)
    print(*C)


mainb()
