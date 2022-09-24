

import sys


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


if __name__ == '__main__':
    agc027_a()
