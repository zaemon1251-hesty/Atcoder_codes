def maina():
    s = int(input())
    # return '%04d' % s)


def mainb():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    # return sum([i < P for i in A]))


def mainc():
    def jd(a, b):
        if a == b:
            return 2
        elif a == "G":
            if b == "C":
                return 0
            elif b == "P":
                return 1
        elif a == "C":
            if b == "G":
                return 1
            elif b == "P":
                return 0
        elif a == "P":
            if b == "G":
                return 0
            elif b == "C":
                return 1

    N, M = map(int, input().split())
    A = []
    for i in range(2*N):
        t = list(input())
        A.append(t)
    rank = list(range(2*N))
    wins = [0]*2*N
    for j in range(M):
        t = [0]*2*N
        for k in range(N):
            a = A[rank[2*k]][j]
            b = A[rank[2*k+1]][j]
            res = jd(a, b)
            if (res == 2):
                pass
            elif (res == 1):
                wins[rank[2*k+1]] -= 1
            else:
                wins[rank[2*k]] -= 1
        rank = sorted(enumerate(wins), key=lambda x: (x[1], x[0]))
        tmp = []
        for item in rank:
            tmp.append(item[0])
        rank = tmp
    for i in rank:
        print(i+1)


def maind():
    mod = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    R = [[0]*3010 for _ in range(N+1)]
    R[0][0] = 1
    A = [0] + A
    B = [0] + B
    for i in range(N+1):
        for j in range(3010):
            if A[i] <= j <= B[i] and i > 0:
                R[i][j] = R[i-1][j] + R[i][j-1]
            elif not (i == j == 0):
                R[i][j] = R[i][j-1]
            R[i][j] %= mod
    print(R[-1][-1] % mod)


maind()
