<<<<<<< HEAD
def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    seen = [False] * N
    X -= 1
    v = X
    while not seen[v]:
        seen[v] = True
        v = A[v] - 1
    print(sum(seen))


if __name__ == '__main__':
    main()
=======
def find(x):
    if P[x] < 0:
        return x
    P[x] = find(P[x])
    return P[x]
def unite(x, y):
    x, y = find(x), find(y)
    if x != y:
        P[x] = y
N = 1 << 20
A, P = [-1]*N, [-1]*N
for _ in range(int(input())):
    t, x = map(int, input().split())
    p = x % N
    if t == 1:
        p = find(p)
        A[p] = x
        unite(p, (p+1) % N)
    else:
        print(A[p])
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
