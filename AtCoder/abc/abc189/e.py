import numpy as np


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    M = int(input())
    op = [list(map(int, input().split())) for _ in range(M)]

    Q = int(input())
    C = [list(map(int, input().split())) for _ in range(Q)]

    a = [np.array([[1, 0], [0, 1]])]
    b = [np.array([0, 0])]
    matrxs = [np.array([[0, 1], [-1, 0]]), np.array([[0, -1], [1, 0]]),
              np.array([[-1, 0], [0, 1]]), np.array([[1, 0], [0, -1]])]
    for t in op:
        if len(t) == 1:
            loc = t[0] - 1
        else:
            loc = t[0] - 1
            if t[0] == 3:
                pl = np.array([2 * t[1], 0])
            else:
                pl = np.array([0, 2 * t[1]])

        n_a = np.dot(matrxs[loc], a[-1])
        n_b = np.dot(matrxs[loc], b[-1])
        if t[0] >= 3:
            n_b = n_b + pl
        a.append(n_a)
        b.append(n_b)
    ans = []
    for num, i in C:
        v = np.array(A[i - 1])
        ans.append(np.dot(a[num], v) + b[num])
    ans = map(lambda x: x.tolist(), ans)
    for x, y in ans:
        print(x, y)


if __name__ == '__main__':
    main()
