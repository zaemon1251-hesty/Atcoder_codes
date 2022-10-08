def agc014_a():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

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
    def input(): return sys.stdin.readline().rstrip()

    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, M, X = mi()
    A = li()
    i = 0
    while A[i] < X:
        i += 1
    print(min(i, M - i))


def abc116_b():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    s = ii()
    Set = set()
    cnt = 1
    while s not in Set:
        Set.add(s)
        s = s // 2 if s % 2 == 0 else 3 * s + 1
        cnt += 1
    print(cnt)


def agc027_a():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, x = mi()
    A = sorted(li(), reverse=True)
    resid = []
    ans = 0
    while A and x >= A[-1]:
        ans += 1
        m = A.pop()
        x -= m
        resid.append(m)
    if x:
        ans -= 1
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
            res += (N // p)
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

    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

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
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

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
        A1 = A[:n >> 1]
        A2 = A[n >> 1:]
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


if __name__ == '__main__':
    arc136_b()
