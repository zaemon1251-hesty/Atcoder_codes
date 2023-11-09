from heapq import heappop, heappush


def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: -x[0])
    day = M
    pq = []
    ans = 0
    while day >= 0:
        while A and A[-1][0] == M - day:
            d, v = A.pop()
            heappush(pq, -v)
        if pq:
            k = heappop(pq)
            ans += -k
        day -= 1
    print(ans)


if __name__ == "__main__":
    main()
