from collections import deque


def zero_index(x):
    return int(x) - 1


inf = 1 << 60


def main():
    N = int(input())
    S = list(map(zero_index, input().split()))
    T = list(map(zero_index, input().split()))
    G = [list(input()) for _ in range(N)]

    if all(x == y for x, y in zip(S, T)):
        print(0)
        exit()

    dist = [[inf] * N for _ in range(N)]
    to = {
        0: (1, 1),
        1: (1, -1),
        2: (-1, 1),
        3: (-1, -1)
    }
    todo = deque([(*S, i) for i in range(4)])
    dist[S[0]][S[1]] = 1
    while todo:
        x, y, t = todo.popleft()
        for k, v in to.items():
            nx, ny = x + v[0], y + v[1]
            nd = dist[x][y] + (0 if t == k else 1)
            op = todo.appendleft if t == k else todo.append
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if G[nx][ny] == '#':
                continue
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                op((nx, ny, k))
    print(dist[T[0]][T[1]] if dist[T[0]][T[1]] < inf else -1)


if __name__ == '__main__':
    main()
