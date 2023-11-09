import sys


def main():
    def input():
        return sys.stdin.readline().rstrip()

    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [0] * (n + 1)
    for i in range(n):
        C[A[i]] += 1
        C[B[i]] += 1

    if max(C) > n:
        print("No")
    else:
        print("Yes")
        B = B[::-1]
        cur = 0
        for i in range(n):
            if A[i] != B[i]:
                continue
            else:
                while A[cur] == B[i] or B[cur] == B[i]:
                    cur += 1
                B[cur], B[i] = B[i], B[cur]
                cur += 1

        print(*B)


if __name__ == "__main__":
    main()
