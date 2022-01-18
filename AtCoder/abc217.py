def maina():
    a, b = map(str, input().split())
    if a < b:
        print("Yes")
    else:
        print("No")


def mainb():
    a, b, c = map(str, input().split())
    g = [a, b, c]
    an = ["abc", "agc", "arc", "ahc"]
    for ans in an:
        if not ans in g:
            print(ans)
            exit()


def mainc():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [-1] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q, sep=" ")


def maind():
    pass


def maine():
    from heapq import heappush, heappop
    from collections import deque
    Q = int(input())
    A = deque([])
    heap = []
    ANS = []
    for _ in range(Q):
        tmp = input()
        if tmp[0] == "1":
            x = int(tmp[2])
            A.append(x)
        elif tmp[0] == "2":
            if len(heap) > 0:
                z = heappop(heap)
            else:
                z = A.popleft()
            ANS.append(z)
        else:
            for i in A:
                heappush(heap, i)
            A = deque([])
    print(*ANS, sep="\n")


maine()
