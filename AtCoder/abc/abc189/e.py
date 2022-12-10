def dot1(mat1, mat2):
    a11, a12, a21, a22 = mat1
    b11, b12, b21, b22 = mat2
    return [a11 * b11 + a12 * b21,
            a11 * b12 + a12 * b22,
            a21 * b11 + a22 * b21,
            a21 * b12 + a22 * b22]


def dot2(mat, vec):
    a11, a12, a21, a22 = mat
    c1, c2 = vec
    return [a11 * c1 + a12 * c2,
            a21 * c1 + a22 * c2]


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    M = int(input())
    op = [list(map(int, input().split())) for _ in range(M)]

    Q = int(input())
    C = [list(map(int, input().split())) for _ in range(Q)]

    a = [[1, 0, 0, 1]]
    b = [[0, 0]]
    matrxs = [
        [0, 1, -1, 0],
        [0, -1, 1, 0],
        [-1, 0, 0, 1],
        [1, 0, 0, -1]
    ]
    for t in op:
        pl = [0, 0]
        loc = t[0] - 1
        if len(t) != 1:
            if t[0] == 3:
                pl = [2 * t[1], 0]
            else:
                pl = [0, 2 * t[1]]
        n_a = dot1(matrxs[loc], a[-1])
        n_b = dot2(matrxs[loc], b[-1])
        n_b[0] += pl[0]
        n_b[1] += pl[1]
        a.append(n_a)
        b.append(n_b)

    ans = []
    for num, i in C:
        v = A[i - 1]
        tmp = dot2(a[num], v)
        tmp[0] += b[num][0]
        tmp[1] += b[num][1]
        ans.append(tmp)
    for x, y in ans:
        print(x, y)


if __name__ == '__main__':
    main()
