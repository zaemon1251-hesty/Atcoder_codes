from functools import reduce
from itertools import combinations


def main():
    N, D = map(int, input().split())
    squares = set([i * i for i in range(1000)])
    X = [list(map(int, input().split())) for _ in range(N)]

    def dist(x, y):
        return sum((xi - yi)**2 for xi, yi in zip(x, y))

    ans = 0
    for i, j in combinations(range(N), 2):
        if dist(X[i], X[j]) in squares:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
