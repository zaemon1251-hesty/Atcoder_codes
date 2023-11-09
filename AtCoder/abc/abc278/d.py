import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = li()
    Q = ii()
    que = [li() for _ in range(Q)]
    modified = [0] * N

    cur_t = -1
    cur_v = 0
    for ts, (t, *buf) in enumerate(que):
        if t == 1:
            x = buf[0]
            cur_t = ts
            cur_v = x
        elif t == 2:
            i, x = buf
            i -= 1
            if modified[i] > cur_t:
                A[i] += x
            else:
                A[i] = cur_v + x
                modified[i] = ts
        else:
            i = buf[0] - 1
            if modified[i] > cur_t:
                print(A[i])
            else:
                print(cur_v)


if __name__ == "__main__":
    main()
