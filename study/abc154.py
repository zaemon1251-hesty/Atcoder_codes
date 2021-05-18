from typing import AnyStr


def maina():
    s, t = map(str, input().split())
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1

    print(a, b)

def mainb():
    print('x'*len(input()))

def mainc():
    n = int(input())
    A = set(list(map(int, input().split())))
    print('YES' if len(A) == n else 'NO')

def maind():
    N, K = map(int, input().split())
    P = list(map(lambda x: (int(x) * (int(x) + 1) // 2) / int(x), input().split()))
    tmp = sum(P[:K])
    ans = tmp
    for i in range(N - K):
        tmp += P[K + i] - P[i]
        ans = max(ans, tmp)

    print(ans)

if __name__ == '__main__':
    #maina()
    #mainb()
    mainc()
    #maind()
