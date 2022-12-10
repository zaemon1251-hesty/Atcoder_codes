from collections import deque


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.reverse()
    C.reverse()
    B = []
    for k in range(M + 1):
        b = C[k] // A[0]
        for i in range(N + 1):
            C[k + i] -= b * A[i]
        B.append(b)
    B.reverse()
    print(*B)


if __name__ == '__main__':
    main()
