def abc299_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = input()
    first = S.index("|")
    second = S.rindex("|")
    for i in range(first + 1, second):
        if S[i] == "*":
            print("in")
            return

    print("out")


def abc299_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, T = mi()
    C = li()
    R = li()

    t_eq = None
    one_eq = None
    for i in range(N):
        if C[i] == T:
            if t_eq is None or R[t_eq] < R[i]:
                t_eq = i
        if C[i] == C[0]:
            if one_eq is None or R[one_eq] < R[i]:
                one_eq = i

    if t_eq is None:
        print(one_eq + 1)
    else:
        print(t_eq + 1)


def abc299_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = input()

    if all(s == "o" for s in S) or all(s == "x" for s in S):
        print(-1)
        return

    pttns = S.split("-")
    pttns = [s for s in pttns if s != ""]

    ans = -1
    for pi in pttns:
        if pi == "":
            continue
        ans = max(ans, len(pi))
    print(ans)


def abc299_d():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()

    def query(i: int):
        print(f"? {i}")
        return ii()

    ok = 1
    ng = N
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if query(cen) == 0:
            ok = cen
        else:
            ng = cen

    print(f"! {ok}")


def abc299_e():
    from collections import deque

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()

    G = [[] for _ in range(N)]

    for _ in range(M):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    dist = [[-1] * N for _ in range(N)]
    for p in range(N):
        seen = [False] * N
        todo = deque([(p, 0)])
        seen[p] = True
        dist[p][p] = 0
        while todo:
            v, d = todo.popleft()
            for nv in G[v]:
                if seen[nv]:
                    continue
                seen[nv] = True
                dist[p][nv] = d + 1
                todo.append((nv, d + 1))

    K = ii()
    que = sorted([li() for _ in range(K)], key=lambda x: x[0], reverse=True)
    white = [False] * N

    # painting stage
    for p, d in que:
        p -= 1
        for nv in range(N):
            white[nv] |= bool(dist[p][nv] < d)

    # check stage
    for p, d in que:
        p -= 1
        valid = False
        for nv in range(N):
            if dist[p][nv] == d and not white[nv]:
                valid = True

        if not valid:
            print("No")
            return

    print("Yes")
    print(*map(lambda x: 1 - x, white), sep="")


def abc296_f():
    from collections import Counter

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    def mergecount(A):
        """転倒数"""

        cnt = 0
        n = len(A)
        if n > 1:
            A1 = A[: n >> 1]
            A2 = A[n >> 1 :]
            cnt += mergecount(A1)
            cnt += mergecount(A2)
            i1 = 0
            i2 = 0
            for i in range(n):
                if i2 == len(A2):
                    A[i] = A1[i1]
                    i1 += 1
                elif i1 == len(A1):
                    A[i] = A2[i2]
                    i2 += 1
                elif A1[i1] <= A2[i2]:
                    A[i] = A1[i1]
                    i1 += 1
                else:
                    A[i] = A2[i2]
                    i2 += 1
                    cnt += n // 2 - i1
        return cnt

    N = ii()
    A = li()
    B = li()
    cA = Counter(A)
    cB = Counter(B)

    if cA != cB:
        print("No")
        return

    if len(cA) == len(cB) == N:
        if (mergecount(A) + mergecount(B)) % 2 == 0:
            print("Yes")
        else:
            print("No")
        return

    print("Yes")


if __name__ == "__main__":
    abc296_f()
