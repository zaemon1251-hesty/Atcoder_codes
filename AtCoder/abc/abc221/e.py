"""
座標圧縮 & imos
"""
from collections import defaultdict

N = int(input())
T = []
Event = defaultdict(int)
Event[0] = 0
Event[pow(10, 100)] = 0
for _ in range(N):
    t = list(map(int, input().split()))
    Event[t[0]] += 1
    Event[t[0] + t[1]] += -1
    T.append(t)
T.sort(key=lambda arr: arr[0])
Event = sorted(Event.items(), key=lambda x: x[0])
ans = [0] * N
for i in range(len(Event)):
    if i == len(Event) - 1:
        continue
    Event[i] = list(Event[i])
    Event[i][1] += Event[i - 1][1]
    num = Event[i][1] - 1
    if num >= 0:
        ans[num] += Event[i + 1][0] - Event[i][0]
print(*ans, sep=" ")
