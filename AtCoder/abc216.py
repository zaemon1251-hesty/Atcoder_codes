def mainc():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 2 == 0:
            N //= 2
            ans += "B"

        else:
            N -= 1
            ans += "A"
    print("".join(list(ans)[::-1]))


def maind():
    from collections import deque
    N, M = map(int, input().split())
    C = [[] for _ in range(N)]
    block = [0] * M
    for i in range(M):
        k = int(input())
        balls = list(map(int, input().split()))
        for j in range(k):
            C[balls[j] - 1].append([i, j])
    C.sort(key=lambda Z: max(Z[0][1], Z[1][1]), reverse=True)
    height = 0
    rest = None
    while C:
        x, y = C.pop()
        if rest:
            C.append(rest)
        if max(x[1], y[1]) > height:
            print('No')
            exit()
        if x[1] - block[x[0]] == y[1] - block[y[0]] == 0:
            rest = None
            block[x[0]] += 1
            block[y[0]] += 1
            height += 1
        else:
            rest = [x, y]
    else:
        print('Yes')


def maine():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A.append(0)
    ans = 0
    for i in range(N):
        if K == 0:
            break
        s = A[i] - A[i+1]
        rest = 0
        if (i + 1)*s > K:
            s = K//(i + 1)
            rest = K % (i + 1)
        adds = (s*A[i] - s*(s-1)//2) * (i + 1)
        if rest != 0:
            adds += (A[i] - s) * rest
        ans += adds
        K -= s * (i + 1) + rest
    print(ans)


maine()
