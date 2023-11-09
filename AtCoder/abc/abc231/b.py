from collections import Counter

N = int(input())
S = [input() for i in range(N)]
ans = ("", 0)
for i, v in Counter(S).items():
    if v > ans[1]:
        ans = (i, v)
print(ans[0])
