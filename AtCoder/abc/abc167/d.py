N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
seen = [False] * N
path = []
cr = 0
while not seen[cr]:
    seen[cr] = True
    path.append(cr)
    cr = A[cr]

chain = path.index(cr)
cycle = len(path) - chain

if K < chain:
    print(path[K]+1)
else:
    K -= chain
    K %= cycle
    print(path[chain + K]+1)
