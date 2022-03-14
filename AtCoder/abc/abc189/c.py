
from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    mini = 0
    maxx = 0
    INF = pow(10, 9)
    for i in range(n):
        mini = INF
        for j in range(i, n):
            mini = min(mini, a[j])
            maxx = max(maxx, mini * (j - i + 1))
    print(maxx)


if __name__ == '__main__':
    main()
