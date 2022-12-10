def main():
    N, Q, X = map(int, input().split())
    W = list(map(int, input().split()))

    sum_w = sum(W)
    dist = [-1] * N
    edge = [-1] * N
    if sum_w == 0:
        print(*[-1] * Q, sep="\n")
        exit()
    dist[0], rest = X // sum_w, X % sum_w
    dist[0] *= N

    edge[0] = 0
    while rest > 0:
        dist[0] += 1
        rest -= W[edge[0]]
        edge[0] = (edge[0] + 1) % N

    now = X - rest
    for i in range(1, N):
        now = now - W[i - 1]
        cnt = 0
        k = edge[i - 1]
        while now < X:
            now += W[k]
            k = (k + 1) % N
            cnt += 1
        dist[i] = dist[i - 1] - 1 + cnt
        edge[i] = k

    seen = [False] * N
    path = []
    cr = 0
    while not seen[cr]:
        seen[cr] = True
        path.append(cr)
        cr = edge[cr]

    chain = path.index(cr)
    cycle = len(path) - chain

    K = [int(input()) for _ in range(Q)]

    for k in K:
        k -= 1
        if k < chain:
            print(dist[path[k]])
        else:
            k -= chain
            k %= cycle
            print(dist[path[chain + k]])


if __name__ == '__main__':
    main()
