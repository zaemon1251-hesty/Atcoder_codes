from collections import deque


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = enumerate(A)
    S = sorted(S, key=lambda x: x[1])
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        G[x].append(y)
    ans = -1 << 60
    seen = [False] * N
    for i, gold in S:
        todo = deque([i])
        while todo:
            p = todo.popleft()
            for nx in G[p]:
                if seen[nx]:
                    continue
                seen[nx] = True
                ans = max(ans, A[nx] - gold)
                todo.append(nx)
    print(ans)


if __name__ == "__main__":
    main()
