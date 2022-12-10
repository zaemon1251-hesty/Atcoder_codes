from itertools import accumulate
import sys
input = sys.stdin.readline


def divisor(n):
    divisors = []
    i = 1
    while i * i < n:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
        i += 1
    if i * i == n:
        divisors.append(i)
    divisors.sort()
    return divisors


N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
for d in divisor(S)[::-1]:
    add = []
    sub = []
    cnt = 0
    for a in A:
        if a % d == 0:
            continue
        cnt += 1
        add.append(d - a % d)
        sub.append(a % d)
    add.sort()
    sub.sort()
    add = [0] + list(accumulate(add))
    sub = [0] + list(accumulate(sub))
    for k in range(cnt + 1):
        if add[k] == sub[cnt - k] and add[k] <= K and sub[cnt - k] <= K:
            print(d)
            exit()
