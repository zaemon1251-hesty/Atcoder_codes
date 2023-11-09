import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import product

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W = mi()
    A = [list(input()) for _ in range(H)]
    B = [list(input()) for _ in range(H)]

    def shift_A_eq_B(s: int, t: int):
        """shift A by (s, t)

        Args:
            s (int): axis 0
            t (int): axis 1
        """
        res = True
        for i in range(H):
            for j in range(W):
                res &= A[(i + s) % H][(j + t) % W] == B[i][j]
        return res

    for s, t in product(range(H), range(W)):
        if shift_A_eq_B(s, t):
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
