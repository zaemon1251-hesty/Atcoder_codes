n = int(input())

pairs = [(i, i) for i in range(1, n + 1)]

i = 1
while i < n:
    l, r = 1, 1 + i
    while r <= n:
        pairs.append((l, r))
        l += 1
        r += 1
    i *= 2

print(len(pairs))
for l, r in pairs:
    print(l, r)

pair_to_idx = {p: i for i, p in enumerate(pairs, start=1)}
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    if l == r:
        a = b = pair_to_idx[(l, l)]
    else:
        i = 1
        while i <= r - l:
            i *= 2
        i /= 2
        a = pair_to_idx[(l, l + i)]
        b = pair_to_idx[(r - i, r)]

    print(a, b)
