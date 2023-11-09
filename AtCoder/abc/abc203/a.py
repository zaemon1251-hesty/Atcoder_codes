a, b, c = map(int, input().split())
if len(set([a, b, c])) == 3:
    print(0)
    exit()
if a == b:
    print(c)
elif b == c:
    print(a)
else:
    print(b)
