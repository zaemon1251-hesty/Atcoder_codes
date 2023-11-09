def main():
    N, X, M = map(int, input().split())
    seen = [False] * M
    s = X
    cnt = 0
    path = []
    while cnt < N and not seen[s]:
        path.append(s)
        seen[s] = True
        s = s**2 % M
        cnt += 1
    if cnt == N:
        print(sum(path))
    else:
        chain = path.index(s)
        cycle = len(path) - chain
        N -= chain
        ans = sum(path[:chain]) + (N // cycle) * sum(path[chain:])
        for _ in range(N % cycle):
            ans += s
            s = s**2 % M
        print(ans)


if __name__ == "__main__":
    main()
