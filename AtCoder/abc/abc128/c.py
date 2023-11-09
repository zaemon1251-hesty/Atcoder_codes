n, m = map(int, input().split())
k = []
s = []
for _ in range(m):
    tmp = list(map(lambda x: int(x) - 1, input().split()))
    k.append(tmp[0] + 1)
    s.append(tmp[1:])
p = list(map(int, input().split()))

count = 0
for i in range(2**n):
    on = []
    lamp = [False] * m
    for j in range(n):
        if (i >> j) & 1:
            on.append(j)

    for la in range(m):
        judge = 0
        for x in on:
            for y in s[la]:
                if x == y:
                    judge += 1
        if judge % 2 == p[la]:
            lamp[la] = True
    if all(lamp):
        count += 1

print(count)
