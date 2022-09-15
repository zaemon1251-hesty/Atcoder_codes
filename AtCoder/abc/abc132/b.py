from itertools import combinations


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N = ii()
    A = li()
    ans = 0
    for i in range(1, N - 1):
        if A[i - 1] < A[i] < A[i + 1] or A[i - 1] > A[i] > A[i + 1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
