x, a, d, n = map(int, input().split())
if d < 0:
    a = a + d * (n - 1)
    d = -d
st = a
fi = a + d * (n - 1)
if x <= st:
    print(abs(x - st))
    exit()
elif x >= fi:
    print(abs(x - fi))
    exit()
elif d == 0:
    print(abs(x - a))
else:
    print(min((x - a) % d, d - (x - a) % d))
