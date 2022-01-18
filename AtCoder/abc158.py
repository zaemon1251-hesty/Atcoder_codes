
def maina():
    S = set(list(input()))
    if len(S) == 2:
        print('Yes')
    else:
        print("No")


def mainb():
    N, A, B = map(int, input().split())
    print((N // (A + B)) * A + min(N % (A + B), A))


def mainc():
    A, B = map(int, input().split())
    for p in range(20000):
        if int(p * 0.08) == A and int(p * 0.1) == B:
            print(p)
            exit()
    print(-1)


def maind():
    from collections import deque
    S = deque(list(input()))
    Q = int(input())
    flg = 0
    for _ in range(Q):
        ipt = input()
        if ipt[0] == "1":
            flg = 1 - flg
        else:
            _, f, c = map(str, ipt.split())
            f = int(f) - 1
            if (f ^ flg) & 1:
                S.append(c)
            else:
                S.appendleft(c)
    if flg == 1:
        S.reverse()
    print("".join(list(S)))


def maine():
    from collections import Counter
    N, P = map(int, input().split())
    A = input()
    T = [0] * N
    power = 1
    if not P in (2, 5):
        A = A[::-1]
        for i in range(N):
            power *= 10
            power %= P
            T[i] = T[i-1] + power * int(A[i])
            T[i] %= P
        counter = Counter(T)
        # counter[0]は 単体で割り切れるので、追加で足す
        print(sum(i * (i - 1) // 2 for i in counter.values()) + counter[0])
    else:
        if P == 5:
            t = {0, 5}
        else:
            t = {0, 2, 4, 6, 8}
        print(sum(int(int(A[i]) in t) * (i + 1) for i in range(N)))


maine()
