from collections import defaultdict, deque


def maina():
    x = int(input())
    print("Yes" if x % 100 == 0 and x != 0 else "No")


def mainb():
    from collections import defaultdict, deque

    x = deque(input())
    s = []
    for i in range(len(x)):
        s.append("".join(x))
        r = x.popleft()
        x.append(r)
    s.sort()
    print(s[0])
    print(s[-1])


mainb()


def mainc():
    N = int(input())
    S = []
    took = 0
    for _ in range(N):
        t = list(map(int, input().split()))
        S.append(t)
        took += t[0]/t[1]
    half = took/2
    i = 0
    ans = 0
    while half > 0:
        tmp = S[i][0]/S[i][1]
        if half > tmp:
            ans += S[i][0]
            half -= tmp
        else:
            ans += S[i][1]*half
            half = 0
        i += 1
    print(ans)


def maind():
    n, m = map(int, input().split())
    N = [0]*n
    A = [list() for _ in range(n)]
    ans = []
    for i in range(m):
        a, b = map(int, input().split())
        N[b-1] += 1
        A[a-1].append(b)
    import heapq
    q = [i+1 for i in range(n) if N[i] == 0]
    heapq.heapify(q)
    while q != []:
        v = heapq.heappop(q)
        ans.append(v)
        for j in A[v-1]:
            N[j-1] -= 1
            if N[j-1] == 0:
                heapq.heappush(q, j)
    if N.count(0) == n:
        print(*ans)
    else:
        print(-1)


def maine():
    def divceil(x, y):
        return (x + y - 1) // y
    x, y, a, b, c = map(int, input().split())
    edge = (x, y)
    rectangle = (a, b, c)
    import itertools
    for i, j in itertools.permutations(edge, r=None):
        if sum(divceil(k, i) for k in rectangle) <= j:
            print("Yes")
            return
    for d, e, f in itertools.permutations(rectangle, r=None):
        for i, j in itertools.permutations(edge, r=None):
            g = j - divceil(d, i)
            if g <= 0:
                continue
            if divceil(e, g) + divceil(f, g) <= i:
                print("Yes")
                return
    print("No")


#
