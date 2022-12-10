a, b = map(int, input().split())
if a == b:
    print(a)
else:
    print(*(set([0,1,2])-set([a, b])))
