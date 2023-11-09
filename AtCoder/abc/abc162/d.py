n = int(input())
s = list(input())
l = n * (n - 1) * (n - 2) // 6
q = {"R": [], "G": [], "B": []}

for i in range(n):
    q[s[i]].append(i)

for k, v in q.items():
    d = len(v)
    l -= d * (d - 1) * (d - 2) // 6
    l -= (n - d) * d * (d - 1) // 2

for i in range(n - 1):
    for k in range(i + 1, n):
        if s[i] != s[k] and (i + k) % 2 == 0 and s[(i + k) // 2] != s[i] and s[(i + k) // 2] != s[k]:
            l -= 1

print(l)
