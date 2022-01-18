N = int(input())
ok = 0
ng = 60
while ng - ok > 1:
    cen = (ok + ng) // 2
    if pow(2, cen) <= N:
        ok = cen
    else:
        ng = cen
print(ok)
