<<<<<<< HEAD
def main():
    s = input()
    t = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    i = t.index(s)
    print(7 - i)


if __name__ == '__main__':
    main()
=======
from math import log10, floor
a, b, x = map(int, input().split())
def check(n):
    if a*n+b*(floor(log10(n))+1) <= x:
        return True
    else:
        return False
ok = 0
ng = 10**9+1
while ng - ok > 1:
    cen = (ok + ng) // 2
    if check(cen):
        ok = cen
    else:
        ng = cen
print(ok)
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
