from functools import reduce
N = int(input())
A = list(map(int, input().split()))
T = reduce(lambda x, y: x ^ y, A)
ans = ""
if N % 2 != 0:
    ans = "Win"
else:
    ans = "Win" if any(i == T for i in A) else "Lose"
print(ans)
c()
