N = int(input())
BITs = [BIT(N) for _ in range(26)]
S = list(map(lambda x: ord(x) - 97, input()))
for i in range(N):
    BITs[S[i]].add(i, 1)
Q = int(input())
for _ in range(Q):
    T, X, Y = input().split()
    if T == '1':
        X = int(X) - 1
        Prev = S[X]
        Now = ord(Y) - 97
        S[X] = Now
        BITs[Prev].add(X, -1)
        BITs[Now].add(X, 1)
    else:
        X = int(X) - 1
        Y = int(Y)
        Ans = 0
        for i in range(26):
            Ans += BITs[i].query(X, Y) > 0
        print(Ans)
e()
