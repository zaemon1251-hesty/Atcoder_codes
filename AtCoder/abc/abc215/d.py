n, m = list(map(int, input().split()))
A = list(map(int, input().split()))


def pFact(a):
    fctrz = []
    x = 2
    while x * x <= a:
        if a % x == 0:
            fctrz.append(x)
            while a % x == 0:
                a //= x
        x += 1
    if a != 1:
        fctrz.append(a)
    return fctrz


prints = []
seive = [True] * (m + 1)
for k in A:
    fctrz = pFact(k)
    for p in fctrz:
        if p <= m and seive[p]:
            i_ = p
            while i_ <= m:
                seive[i_] = False
                i_ += p
for i in range(1, m + 1):
    if seive[i]:
        prints.append(i)
print(len(prints))
for p in prints:
    print(p)
