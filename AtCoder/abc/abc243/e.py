

def main():
    N, M = map(int, input().split())
    inf = 1 << 60
    dist = [inf] * N
    G = [[] for _ in range(N)]
    E = []
    use_ = {}
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        E.append((a, b, c))
        use_[(a, b)] = False
        G[a].append(b)
        G[b].append(a)
    E.sort(key=lambda x: x[2], reverse=True)
    p = 0


if __name__ == '__main__':
    main()
