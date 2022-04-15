N = int(input())
ans = N
s = set()
for a in range(2, 10**5):
    i = 2
    while pow(a, i) <= N:
        s.add(pow(a, i))
        i += 1
print(ans- len(s))
