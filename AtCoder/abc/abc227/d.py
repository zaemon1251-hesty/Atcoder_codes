n, k = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, sum(a)//k+1
while l+1 < r:
    c = (l+r)//2
    s = 0
    for v in a:
        s += min(v, c)
    if s < k*c:
        r = c
    else:
        l = c
print(l)
_name__ == '__main__':
maind()
