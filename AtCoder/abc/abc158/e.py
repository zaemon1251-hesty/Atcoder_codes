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
        T[i] = T[i - 1] + power * int(A[i])
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
e()
