from collections import deque


def main():
    inf = 1 << 60
    N = int(input())
    P = []
    x = []
    y = []
    for _ in range(N):
        x1, y1, p = map(int, input().split())
        x.append(x1)
        y.append(y1)
        P.append(p)

    def check(s):
        for i in range(N):
            seen = [False] * N
            todo = deque([i])
            seen[i] = True
            while todo:
                v = todo.popleft()
                for j in range(N):
                    if v == j or seen[j]:
                        continue
                    if s * P[v] >= abs(x[v] - x[j]) + abs(y[v] - y[j]):
                        seen[j] = True
                        todo.append(j)
            if all(seen):
                return True

        return False

    ok = 10**18
    ng = 0
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
    print(ok)


if __name__ == '__main__':
    main()
