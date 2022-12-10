n = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))


def swap(AB, i):
    if AB == "A":
        P[i], P[i + 1] = P[i + 1], P[i]
    else:
        P[i], P[i + 2] = P[i + 2], P[i]


ans = []

for i in range(n):
    if i % 2 == P[i] % 2:
        continue
    while i >= 2 and P[i - 2] % 2 == i % 2:
        ans.append(("B", i - 2))
        swap("B", i - 2)
        i -= 2

for i in range(0, n, 2):
    if i % 2 == P[i] % 2:
        continue
    ans.append(("A", i))
    swap("A", i)

for i in range(n):
    j = P.index(i)
    while i < j:
        ans.append(("B", j - 2))
        swap("B", j - 2)
        j -= 2

ans = [(i, a + 1) for i, a in ans]

print(len(ans))
for ans_sub in ans:
    print(*ans_sub)
