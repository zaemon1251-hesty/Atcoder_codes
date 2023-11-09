from collections import deque
from heapq import heappop, heappush
from itertools import product
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

    N, K = mi()
    D = li()
    ans = 0
    for l_cnt, r_cnt in product(range(K + 1), repeat=2):
        if l_cnt + r_cnt > min(K, N):
            continue
        que = deque(D.copy())
        bag = []

        for _ in range(l_cnt):
            heappush(bag, que.popleft())

        for _ in range(r_cnt):
            heappush(bag, que.pop())

        total = sum(bag)
        res = total
        deleted = 0
        rest = K - l_cnt - r_cnt

        while rest > 0 and bag:
            deleted += heappop(bag)
            res = max(res, total - deleted)
            rest -= 1
        ans = max(res, ans)

    print(ans)


if __name__ == "__main__":
    main()
