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
