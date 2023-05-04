def maine():
    from math import ceil, floor
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        if i > N:
            print(ans)
            exit()
        ans += i * (floor(N/i) - ceil(N/(i+1)) + 1 - int(N % (i+1) == 0))
    for i in range(1, floor(N/10**6)+1):
        ans += floor(N/i)
    print(ans)


def maind():
    N, D = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort(key=lambda x: (x[1]))
    removed = -1
    ans = 0

    for a, b in S:
        # a が removed より大きい = まだ取り除いてない
        if a > removed:
            removed = b + D - 1
            ans += 1
    print(ans)


def mainc():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    a, b, c, d = max(1-A, 1-B), min(N-A, N-B), max(1-A, B-N), min(N-A, B-1)
    G = [["0"]*(S-R+1) for _ in range(Q-P+1)]
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            t = "."
            if (i-A == j-B and a <= i-A <= b) or (i-A == -(j-B) and c <= i-A <= d):
                t = "#"
            G[i-P][j-R] = t
    for i in range(Q-P+1):
        G[i] = "".join(G[i])
    print(*G, sep="\n")


mainc()