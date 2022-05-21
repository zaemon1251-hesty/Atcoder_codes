from heapq import heappop, heappush, heapify


def main():
    N, M = map(int, input().split())
    A = list(map(lambda xx: -int(xx), input().split()))
    heapify(A)
    while M and A:
        x = heappop(A)
        x *= -1
        x //= 2
        M -= 1
        if x > 0:
            heappush(A, -x)
    print(A)
    print(-sum(A))


if __name__ == '__main__':
    main()
