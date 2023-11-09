from bisect import bisect, bisect_left


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [[] for _ in range(N + 1)]
    for i in range(N):
        cnt[A[i]].append(i)
    Q = int(input())
    ans = []
    for _ in range(Q):
        l, r, x = map(int, input().split())
        l -= 1
        r -= 1
        idl = bisect_left(cnt[x], l)
        idr = bisect(cnt[x], r)
        ans.append(idr - idl)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
