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

    dist = [[[inf] * 4 for _ in range(N)] for _ in range(N)]
    to = {
        0: (1, 1),
        1: (1, -1),
        2: (-1, -1),
        3: (-1, 1)
    }
    todo = deque([])
    for i in range(4):
        todo.append((*S, i))
        dist[S[0]][S[1]][i] = 1
    while todo:
        x, y, t = todo.popleft()
        for k, v in to.items():
            nx, ny = x + v[0], y + v[1]
            nd = dist[x][y][t] + (0 if t % 2 == k % 2 else 1)
            op = todo.appendleft if t % 2 == k % 2 else todo.append
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if G[nx][ny] == '#':
                continue
            if dist[nx][ny][k] > nd:
                dist[nx][ny][k] = nd
                op((nx, ny, k))
    print(min(dist[T[0]][T[1]]) if min(dist[T[0]][T[1]]) < inf else -1)


if __name__ == '__main__':
    main()
