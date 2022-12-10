from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, K = mi()
    ans = []
    for i in range(1, N):
        ans.append([0, i])

    k = (N - 1) * (N - 2) // 2
    if (k < K):
        print(-1)
        exit()

    for i, j in combinations(range(1, N), 2):
        if k == K:
            break
        ans.append([i, j])
        k -= 1

    n = len(ans)
    print(n)
    for a, b in ans:
        print(a + 1, b + 1)


if __name__ == '__main__':
    main()
