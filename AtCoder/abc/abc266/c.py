from itertools import combinations


def sub(a, b):
    return [a[0] - b[0], a[1], b[1]]


def signedArea(a, b, c):
    x0, y0 = a
    x1, y1 = b
    x2, y2 = c
    return 1 / 2 * (x0 * y1 + x1 * y2 + x2 * y0 - y0 * x1 - y1 * x2 - y2 * x0)


def main():
    A = [list(map(int, input().split())) for _ in range(4)]
    cmbs = [0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]
    for i, j, k in cmbs:
        if signedArea(A[i], A[j], A[k]) < 0:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
