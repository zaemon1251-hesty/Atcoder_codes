from itertools import product


def main():
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]
    ma = max(max(a) for a in A)
    sts = []
    cand = ""
    ng = {(-1, -1), (N, -1), (-1, N), (N, N)}
    for i in range(N):
        for j in range(N):
            if A[i][j] == ma:
                sts.append([i, j])

    for st in sts:
        ans = str(ma)
        prev = set()
        while len(ans) < N:
            i, j = st
            res = -1
            for dx, dy in product(range(-1, 2), repeat=2):
                if dx == dy == 0:
                    continue

                nx, ny = i + dx, j + dy

                if (nx, ny) in ng:
                    continue

                nx, ny = (N + nx) % N, (N + ny) % N

                if (nx, ny) in prev:
                    continue

                if A[nx][ny] > res:
                    res = A[nx][ny]
                    st = [nx, ny]

            prev.add((i, j))
            ans += str(res)

        cand = max(ans, cand)
    print(cand)


if __name__ == '__main__':
    main()
