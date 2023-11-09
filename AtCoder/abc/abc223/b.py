from collections import defaultdict, deque

x = deque(input())
s = []
for i in range(len(x)):
    s.append("".join(x))
    r = x.popleft()
    x.append(r)
s.sort()
print(s[0])
print(s[-1])
b()
