from itertools import permutations
from math import sqrt


def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    D = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            D[i][j] = sqrt((S[i][0] - S[j][0]) ** 2 + (S[i][1] - S[j][1]) ** 2)

    lengths = []
    for paths in permutations(range(N), N):
        tmp = 0
        for i in range(N - 1):
            tmp += D[paths[i]][paths[i - 1]]
        lengths.append(tmp)

    print(sum(lengths) / len(lengths))

if __name__ == '__main__':
    main()
