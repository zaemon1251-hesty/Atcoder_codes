from collections import defaultdict
from heapq import heappop, heappush
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    prime_factorizations = defaultdict(list)

    for i in range(N):
        m = int(input())
        for _ in range(m):
            p, cnt = map(int, input().split())
            heappush(prime_factorizations[p], [-cnt, i])

    responsibles = set()
    for p, heap_p in prime_factorizations.items():

        maxcnt, idx = heappop(heap_p)
        if heap_p:
            secondcnt, _ = heappop(heap_p)
            if maxcnt == secondcnt:
                continue

        responsibles.add(idx)

    print(min(len(responsibles) + 1, N))


if __name__ == '__main__':
    main()
