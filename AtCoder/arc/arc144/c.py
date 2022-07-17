import sys


def resolve() -> None:
    N, K = (int(x) for x in sys.stdin.readline().strip().split())
    if (N >> 1) < K:
        print(-1)
        return

    ans = list(range(1, N + 1))
    for i in range(0, N, 2 * K):
        for j in range(K):
            if i + j + K >= N:
                break
            ans[i + j], ans[i + j + K] = ans[i + j + K], ans[i + j]
        else:
            continue
        break

    res = N % (2 * K)
    if res != 0:
        last = sorted(ans[-2 * K:])
        for i in range(N - 2 * K, N):
            ans[i] = last[(i - N + 2 * K + K) % (2 * K)]

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    resolve()
