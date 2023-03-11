import sys


def main():
    input = sys.stdin.readline
    N, M = [int(x) for x in input().strip().split()]
    directs = [list() for _ in range(N)]
    cnt = [0] * N
    ans = [0] * N
    for m in range(M):
        x, y = [int(x) for x in input().strip().split()]
        directs[x - 1].append(y)
        cnt[y - 1] += 1
    s = 0
    for i, c in enumerate(cnt):
        if c == 0:
            if s:
                print('No')
                exit()
            s = i + 1
    c = 1
    while s > -1:
        ans[s - 1] = c
        c += 1
        p = -1
        for n in directs[s - 1]:
            cnt[n - 1] -= 1
            if cnt[n - 1] == 0:
                if p != -1:
                    print('No')
                    exit()
                p = n
        s = p

    print('Yes')
    print(*ans)


if __name__ == '__main__':
    main()
