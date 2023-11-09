from cgitb import reset


def agc014_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    def divs(*args):
        a, b, c = args
        return (b // 2 + c // 2, c // 2 + a // 2, a // 2 + b // 2)

    A, B, C = mi()
    arg = (A, B, C)
    ans = 0
    ac = set()
    while all(i % 2 == 0 for i in arg):
        if arg in ac:
            print(-1)
            exit()
        ac.add(arg)
        arg = divs(*arg)
        ans += 1
    print(ans)


def abc094_b():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M, X = mi()
    A = li()
    i = 0
    while A[i] < X:
        i += 1
    print(min(i, M - i))


def abc116_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    s = ii()
    Set = set()
    cnt = 1
    while s not in Set:
        Set.add(s)
        s = s // 2 if s % 2 == 0 else 3 * s + 1
        cnt += 1
    print(cnt)


def agc027_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, x = mi()
    A = sorted(li(), reverse=True)
    if sum(A) == x:
        print(N)
    elif sum(A) < x:
        print(N - 1)
    else:
        ans = 0
        while x >= A[-1]:
            x -= A.pop()
            ans += 1
        print(ans)


def arc067_a():
    def get_prime(n, get_sieve=False):
        prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if prime[i]:
                for j in range(i * 2, n, i):
                    prime[j] = False
        if get_sieve:
            return [i for i in range(2, n) if prime[i]]
        else:
            return prime

    N = int(input())
    primes = get_prime(N + 10)
    facts = []
    for i in range(2, N + 1):
        if not primes[i]:
            continue
        p = i
        t = 1
        res = 0
        while p <= N:
            res += N // p
            p *= i
            t += 1
        facts.append(res + 1)

    ans = 1
    MOD = 10**9 + 7
    for f in facts:
        ans *= f
        ans %= MOD
    print(ans)


def arc066_a():
    from collections import Counter

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = li()
    if N % 2 != 0:
        A.remove(0)
    cnt = Counter(A)

    if N % 2 == 0:
        ideal = [i for i in range(1, N, 2)]
    else:
        ideal = [i for i in range(2, N, 2)]
    if not all(cnt[i] == 2 for i in ideal):
        print(0)
    else:
        MOD = 10**9 + 7
        print(pow(2, len(ideal), MOD))


def abc085_d():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, H = mi()
    S = [li() for _ in range(N)]
    W = []
    for i, (a, b) in enumerate(S):
        W.append((a, i, 0))
        W.append((b, i, 1))
    W.sort(key=lambda x: (x[0], -x[2]), reverse=True)

    ans = 0
    cur = H
    for damage, _, q in W:
        if q == 0:
            ans += (cur + damage - 1) // damage
            print(ans)
            exit()
        else:
            cur -= damage
            ans += 1
            if cur <= 0:
                print(ans)
                exit()


def agc056_a():
    N = int(input())
    ans = []
    for i in range(N):
        ans_i = ["."] * N
        ans_i[(3 * i) % N] = "#"
        ans_i[(3 * i + 1) % N] = "#"
        ans_i[(3 * i + 2) % N] = "#"
        ans.append(ans_i)

    if N % 3 != 0:
        ans[0], ans[N // 3 - 1] = ans[N // 3 - 1], ans[0]
        ans[N - 1], ans[N - N // 3] = ans[N - N // 3], ans[N - 1]

    for i in range(N):
        print(*ans[i], sep="")


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


def arc136_b():
    from collections import Counter

    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    SA = Counter(A)
    SB = Counter(B)

    if SA != SB:
        print("No")
        return

    if any(v > 1 for v in SA.values()):
        print("Yes")
        return

    if mergecount(A) % 2 == mergecount(B) % 2:
        print("Yes")
        return

    print("No")
    return


def abc092_b():
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    days = [0] * (D + 1)
    for a in A:
        for k in range(1, D + 1, a):
            days[k] += 1
    print(X + sum(days))


def hitachi2020_b():
    from math import inf

    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = inf
    for _ in range(M):
        x, y, c = map(int, input().split())
        ans = min(ans, a[x - 1] + b[y - 1] - c)
    a.sort()
    b.sort()
    ans = min(ans, a[0] + b[0])
    print(ans)


def abc114_b():
    from math import inf

    s = input()
    n = len(s)
    ans = inf
    for i in range(n - 2):
        ans = min(ans, abs(int(s[i : i + 3]) - 753))
    print(ans)


def abc108_b():
    x1, y1, x2, y2 = map(int, input().split())
    vec = (x2 - x1, y2 - y1)
    x3, y3 = x2 - vec[1], y2 + vec[0]
    vec = (x3 - x2, y3 - y2)
    x4, y4 = x3 - vec[1], y3 + vec[0]
    print(x3, y3, x4, y4)


def abc063_b():
    s = list(input())
    print("yes" if len(s) == len(set(s)) else "no")


def abc052_b():
    from itertools import accumulate

    N = int(input())
    S = map(lambda x: 1 if x == "I" else -1, input())
    S = accumulate([0] + list(S))
    print(max(list(S)))


def abc084_b():
    A, B = map(int, input().split())
    S = input()
    S = S.split("-")
    if len(S) == 2 and len(S[0]) == A and len(S[1]) == B:
        print("Yes")
    else:
        print("No")


def abc087_b():
    from itertools import product

    ans = 0
    A, B, C, X = int(input()), int(input()), int(input()), int(input())
    for a, b, c in product(range(A + 1), range(B + 1), range(C + 1)):
        if 500 * a + 100 * b + 50 * c == X:
            ans += 1
    print(ans)


def abc071_b():
    from string import ascii_lowercase

    cnt = {a: 0 for a in ascii_lowercase}
    s = input()
    for w in s:
        cnt[w] += 1
    for a in ascii_lowercase:
        if cnt[a] == 0:
            print(a)
            exit()
    else:
        print("None")


def abc127_c():
    N, M = map(int, input().split())
    cards = [0] * (N + 1)
    for _ in range(M):
        l, r = map(int, input().split())
        cards[l - 1] += 1
        cards[r] -= 1

    for i in range(1, N):
        cards[i] += cards[i - 1]

    ans = sum(card >= M for card in cards)
    print(ans)


def agc036_a():
    S = int(input())
    x1, y1 = 0, 0
    x2, y2 = 10**9, 1
    y3, x3 = divmod(S, x2)
    if x3 != 0:
        y3 += 1
        x3 = 10**9 - x3
    print(x1, y1, x2, y2, x3, y3)


def ddcc2020_qual_c():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = [[-1] * W for _ in range(H)]

    row_divides = []
    for x in range(H):
        if "#" in S[x]:
            row_divides.append(x)

    cols = []
    for x in row_divides:
        col_divides = []
        for y in range(W):
            if S[x][y] == "#":
                col_divides.append(y)
        col_divides.append(W)  # 門番

        cols.append(col_divides)

    colors = 1
    x = 0
    for sx, coldivs in zip(row_divides, cols):
        y = 0
        for sy in coldivs[1:]:
            while y < W and y < sy:
                ans[sx][y] = colors
                y += 1
            colors += 1

        while x < sx:
            for y in range(W):
                ans[x][y] = ans[sx][y]
            x += 1
        x += 1

    if x < H:
        for i in range(x, H):
            for y in range(W):
                ans[i][y] = ans[sx][y]

    for row in ans:
        print(*row)


if __name__ == "__main__":
    ddcc2020_qual_c()
