import sys
from itertools import accumulate
inf = 1 << 32


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    N, M, K = mi()
    S = input()
    sumS = [0] + list(accumulate(map(lambda x: 1 if x == "x" else 0, S)))
    x = S.count("x")

    def get_sum(start, end):
        """閉区間 [start, end) の合計を求める

        Args:
            start (int): included start
            end (int): excluded end

        Returns:
            int: [start, end)の”ｘ”の合計
        """
        if end <= N:
            return sumS[end] - sumS[start]

        rep = max(0, end - start - (N - start) - (end % N)) // N
        head = sumS[N] - sumS[start]
        tail = sumS[end % N]

        return rep * x + head + tail

    def length(start):
        ok = start + 1
        ng = N * M + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if get_sum(start, mid) <= K:
                ok = mid
            else:
                ng = mid
        return ok - start

    ans = -inf
    for i in range(N):
        ans = max(ans, length(i))
    print(ans)


if __name__ == '__main__':
    main()
