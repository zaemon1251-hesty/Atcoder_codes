from collections import deque
from math import inf


def main():
    N, M = map(int, input().split())
    S = list(map(int, list(input())))
    i = N
    ans = []
    while i:
        for j in range(min(M, i), 0, -1):
            if S[i - j] == 0:
                ans.append(j)
                i -= j
                break
        else:
            print(-1)
            exit()
        continue
    print(*ans[::-1])


if __name__ == "__main__":
    main()
