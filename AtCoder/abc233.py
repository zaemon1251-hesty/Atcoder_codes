def maina():
    X, Y = map(int, input().split())
    from math import ceil
    print(max(0, ceil((Y - X) / 10)))


def mainb():
    L, R = map(int, input().split())
    S = list(input())
    L -= 1
    A = S[:L] + S[L:R][::-1] + S[R:]
    print("".join(A))


def mainc():
    from itertools import product
    from functools import reduce
    N, X = map(int, input().split())
    La = [list(map(int, input().split())) for _ in range(N)]
    L = [i[0] for i in La]
    a = [i[1:] for i in La]
    ans = 0
    for items in product(*a):
        if reduce(lambda x, y: x * y, items) == X:
            ans += 1
    print(ans)


def maind():
    from collections import defaultdict, Counter
    from itertools import accumulate
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    acc = list(accumulate(A))
    acc.insert(0, 0)
    C = Counter(acc)

    ans = 0
    if K != 0:
        for i in range(N + 1):
            ans += C[acc[i] + K]
            C[acc[i]] -= 1
    else:
        for key, value in C.items():
            ans += (value * (value - 1)) // 2
    print(ans)


maind()


def maine():
    # 桁DP
    # 大きな数字(10^500000レベル)の加算処理を文字列で行う
    X = input()
    N = len(X)

    dp = list(map(int, list(X)))
    for i in range(1, N):
        dp[i] += dp[i - 1]

    ans = []
    carry = 0
    for keta in reversed(dp):
        keta += carry
        carry = keta // 10
        ans.append(keta % 10)

    if carry > 0:
        ans.append(carry)

    print(''.join(map(str, ans[::-1])))


maine()
